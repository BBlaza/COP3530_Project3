from db import get_cursor

def search():
    pass



def search_by_title(title):
    cur = get_cursor()
    cur.execute("SELECT * FROM movies WHERE primary_title = %s;", (title,))
    rows = cur.fetchall()
    cur.close()
    return rows