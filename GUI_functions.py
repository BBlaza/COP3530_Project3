from db import get_cursor
import elements
import time
import SQLite

def Btree_search():
    pass
    title = elements.search_entry.get().strip()

    min_runtime, max_runtime = 0, 0
    if (elements.duration_range_combo.get() == 'less than 30 min'):
        min_runtime = 0
        max_runtime = 29
    elif (elements.duration_range_combo.get() == '31-59 min'):
        min_runtime = 30
        max_runtime = 59
    elif (elements.duration_range_combo.get() == '1-2 hours'):
        min_runtime = 60
        max_runtime = 119
    elif (elements.duration_range_combo.get() == '2-3 hours'):
        min_runtime = 120
        max_runtime = 179
    elif (elements.duration_range_combo.get() == '3-5 hours'):
        min_runtime = 180
        max_runtime = 299
    elif (elements.duration_range_combo.get() == '5-10 hours'):
        min_runtime = 300
        max_runtime = 599
    elif (elements.duration_range_combo.get() == 'more than 10 hours'):
        min_runtime = 600
        max_runtime = 0

    min_release_date = elements.release_scale_min.get()
    max_release_date = elements.release_scale_max.get()

    genre = elements.genre_combo.get()

    lowest_rate = elements.rating_scale_min.get()
    highest_rate = elements.rating_scale_max.get()

    if (min_release_date > max_release_date) or (lowest_rate > highest_rate):
        elements.log_label.config(text="Maximum cannot be greater than minimum", fg="red")
        return

    cur = get_cursor()
    query = (
        "SELECT tconst, title_type, primary_title, start_year, runtime_minutes, genres, rating "
        "FROM movies "
        "WHERE primary_title ILIKE %s"
    )
    params = [f"%{title}%"]

    if genre:
        query += " AND genres ILIKE %s"
        params.append(f"%{genre}%")

    if min_release_date:
        query += " AND start_year >= %s"
        params.append(min_release_date)

    if max_release_date:
        query += " AND start_year <= %s"
        params.append(max_release_date)

    if elements.take_null_rating_var.get():
        # Accept NULLs + filter the ones that have ratings
        if lowest_rate:
            query += " AND (rating IS NULL OR rating >= %s)"
            params.append(lowest_rate)
        if highest_rate:
            query += " AND (rating IS NULL OR rating <= %s)"
            params.append(highest_rate)
    else:
        # Ignore NULLs entirely
        query += " AND rating IS NOT NULL"
        if lowest_rate:
            query += " AND rating >= %s"
            params.append(lowest_rate)
        if highest_rate:
            query += " AND rating <= %s"
            params.append(highest_rate)

    if min_runtime:
        query += " AND runtime_minutes >= %s"
        params.append(min_runtime)

    if max_runtime:
        query += " AND runtime_minutes <= %s"
        params.append(max_runtime)

    # Limit results
    query += " LIMIT 100"

    start_time = time.time()

    # Execute query
    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    end_time = time.time()
    duration = end_time - start_time
    elements.log_label.config(text=f"Search completed in {duration:.3f} seconds", fg="black")

    # clear old results
    for item in elements.results_tree.get_children():
        elements.results_tree.delete(item)

    # insert new ones
    for row in rows:
        elements.results_tree.insert("", "end", values=row)


def Bptree_search():
    db = SQLite.MovieDatabaseSQLite('movies.db', 'title.basics.tsv.gz')
    #db.load_ratings('title.ratings.tsv.gz')

    title = elements.search_entry.get().strip()

    min_runtime, max_runtime = 0, 0
    if (elements.duration_range_combo.get() == 'less than 30 min'):
        min_runtime = 0
        max_runtime = 29
    elif (elements.duration_range_combo.get() == '31-59 min'):
        min_runtime = 30
        max_runtime = 59
    elif (elements.duration_range_combo.get() == '1-2 hours'):
        min_runtime = 60
        max_runtime = 119
    elif (elements.duration_range_combo.get() == '2-3 hours'):
        min_runtime = 120
        max_runtime = 179
    elif (elements.duration_range_combo.get() == '3-5 hours'):
        min_runtime = 180
        max_runtime = 299
    elif (elements.duration_range_combo.get() == '5-10 hours'):
        min_runtime = 300
        max_runtime = 599
    elif (elements.duration_range_combo.get() == 'more than 10 hours'):
        min_runtime = 600
        max_runtime = 0

    min_release_date = elements.release_scale_min.get()
    max_release_date = elements.release_scale_max.get()

    genre = elements.genre_combo.get()

    lowest_rate = elements.rating_scale_min.get()
    highest_rate = elements.rating_scale_max.get()

    if (min_release_date > max_release_date) or (lowest_rate > highest_rate):
        elements.log_label.config(text="Maximum cannot be greater than minimum", fg="red")
        return
    executionTime = [1]
    rows = db.get_movies_by_filters(executionTime, genre=genre,lowestRuntime=min_runtime, highestRuntime=max_runtime, movieName=title, ratingMin=lowest_rate, ratingMax=highest_rate, startingYear=min_release_date, endingYear=max_release_date)

    elements.log_label.config(text=f"Search completed in {executionTime[0]:.3f} seconds", fg="black")

    for item in elements.results_tree.get_children():
        elements.results_tree.delete(item)

    for row in rows:
        elements.results_tree.insert("", "end", values=row)

    db.close()