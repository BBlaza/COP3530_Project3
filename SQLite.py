import gzip
import csv
import sqlite3
from datetime import datetime

class MovieDatabaseSQLite:
    def __init__(self, db_name, tsv_gz_file):
        self.conn = sqlite3.connect(db_name)
        self.tsv_gz_file = tsv_gz_file
        

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                tconst TEXT PRIMARY KEY,
                titleType TEXT,
                primaryTitle TEXT,
                originalTitle TEXT,
                isAdult INTEGER,
                startYear INTEGER,
                endYear INTEGER,
                runtimeMinutes TEXT,
                genres TEXT,
                averageRating REAL
            )
        ''')
        self.conn.commit()

    def read_tsv_gz(self):
        with gzip.open(self.tsv_gz_file, 'rt', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                yield row

    def load_data(self):
        cursor = self.conn.cursor()
        count = 0
        for row in self.read_tsv_gz():
           
            try:
                cursor.execute('''
                    INSERT OR IGNORE INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    row['tconst'],
                    row['titleType'],
                    row['primaryTitle'],
                    row['originalTitle'],
                    int(row['isAdult']) if row['isAdult'] != '\\N' else 0,
                    int(row['startYear']) if row['startYear'] != '\\N' else None,
                    int(row['endYear']) if row['endYear'] != '\\N' else None,
                    row['runtimeMinutes'],
                    row['genres'],
                    None
                ))
                count += 1
                if count % 10000 == 0:
                    print(f"Inserted {count} rows...")
            except Exception as e:
                print(f"Skipping row due to error: {e}")
        self.conn.commit()
        print(f"Finished inserting {count} rows.")
       

        
    def load_ratings(self, ratings_file):
        with gzip.open(ratings_file, 'rt', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            cursor = self.conn.cursor()
            for row in reader:
                tconst = row['tconst']
                rating = row['averageRating']
                try:
                    cursor.execute('''
                        UPDATE movies
                        SET averageRating = ?
                        WHERE tconst = ?
                    ''', (float(rating), tconst))
                except Exception as e:
                    print(f"Error updating rating for {tconst}: {e}")
            self.conn.commit()

    def get_movies_by_filters(self,executionTime, genre='',lowestRuntime = None, highestRuntime = None, startingYear=None, endingYear=None, movieName=None, ratingMin=None, ratingMax=None):
        cursor = self.conn.cursor()

        query = '''
            SELECT tconst, titleType, primaryTitle, startYear, runtimeMinutes, genres, averageRating
            FROM movies
            WHERE 1=1
        '''
        params = []
        

        if genre:
            query += ' AND genres LIKE ?'
            params.append(f'%{genre}%')

        if lowestRuntime:
            query += ' AND runtimeMinutes >= ?'
            params.append(lowestRuntime)
            query += ' AND runtimeMinutes <= ?'
            params.append(highestRuntime)
        
        if movieName:
            query += ' AND primaryTitle LIKE ?'
            params.append(f'%{movieName}%')

        if startingYear is not None:
            query += ' AND startYear >= ?'
            params.append(startingYear)

        if endingYear is not None:
            query += ' AND startYear <= ?'
            params.append(endingYear)

        if ratingMin is not None:
            query += ' AND averageRating >= ?'
            params.append(ratingMin)

        if ratingMax is not None:
            query += ' AND averageRating <= ?'
            params.append(ratingMax)


        query += ' ORDER BY primaryTitle LIMIT 100'
        startTime = datetime.now()


        cursor.execute(query, params)
        executionTime[0] = datetime.now()-startTime
        return cursor.fetchall()


    def close(self):
        self.conn.close()
