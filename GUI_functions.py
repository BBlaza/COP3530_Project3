# Btreefunctions.py
from db import get_cursor
import elements

def search():
    title = elements.search_entry.get().strip()
    if not title:
        return

    cur = get_cursor()
    cur.execute(
        "SELECT tconst, title_type, primary_title, start_year, genres "
        "FROM movies WHERE primary_title ILIKE %s LIMIT 100;",
        (f"%{title}%",)
    )
    rows = cur.fetchall()
    cur.close()

    # clear old results
    for item in elements.results_tree.get_children():
        elements.results_tree.delete(item)

    # insert new ones
    for row in rows:
        elements.results_tree.insert("", "end", values=row)