from db import get_cursor
import elements

def Btree_search():
    title = elements.search_entry.get().strip()
    if not title:
        return

    min_runtime, max_runtime = 0, 0
    if (elements.duration_range_combo.get() == 'less than 30 hours'):
        min_runtime = -1
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
        max_runtime = 5999
    elif (elements.duration_range_combo.get() == 'more than 10 hours'):
        min_runtime = 6000
        max_runtime = 9999999

    min_release_date = elements.release_scale_min.get()
    max_release_date = elements.release_scale_max.get()

    genre = elements.genre_combo.get()

    lowest_rate = elements.rating_scale_min.get()
    highest_rate = elements.rating_scale_max.get()

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

    # Execute query
    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()

    # clear old results
    for item in elements.results_tree.get_children():
        elements.results_tree.delete(item)

    # insert new ones
    for row in rows:
        elements.results_tree.insert("", "end", values=row)

def Bptree_search():
    pass