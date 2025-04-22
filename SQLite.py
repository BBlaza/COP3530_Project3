import gzip
import csv
import sqlite3

class MovieDatabaseSQLite:
    def __init__(self, db_name, tsv_gz_file):
        self.conn = sqlite3.connect(db_name)
        self.tsv_gz_file = tsv_gz_file
        self.create_table()
        self.load_data()

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
                genres TEXT
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
        for row in self.read_tsv_gz():
            try:
                cursor.execute('''
                    INSERT OR IGNORE INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    row['tconst'],
                    row['titleType'],
                    row['primaryTitle'],
                    row['originalTitle'],
                    int(row['isAdult']) if row['isAdult'] != '\\N' else 0,
                    int(row['startYear']) if row['startYear'] != '\\N' else None,
                    int(row['endYear']) if row['endYear'] != '\\N' else None,
                    row['runtimeMinutes'],
                    row['genres']
                ))
            except Exception as e:
                print(f"Skipping row due to error: {e}")
        self.conn.commit()

    def get_movies_by_genre_year(self, genre, year):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT primaryTitle, startYear, genres
            FROM movies
            WHERE genres LIKE ? AND startYear = ?
            ORDER BY primaryTitle
        ''', (f'%{genre}%', year))
        return cursor.fetchall()

    def get_movies_by_multiple_genres(self, genres, year=None):
        cursor = self.conn.cursor()
        query = '''
            SELECT primaryTitle, startYear, genres
            FROM movies
            WHERE 1 = 1
        '''
        params = []

        for genre in genres:
            query += ' AND genres LIKE ?'
            params.append(f'%{genre}%')

        if year is not None:
            query += ' AND startYear = ?'
            params.append(year)

        query += ' ORDER BY primaryTitle'
        cursor.execute(query, params)
        return cursor.fetchall()

    def close(self):
        self.conn.close()
