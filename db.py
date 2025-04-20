# db.py
import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


DB_NAME = os.getenv("PGDATABASE")
DB_USER = os.getenv("PGUSER")
DB_PASS = os.getenv("PGPASSWORD")
DB_HOST = os.getenv("PGHOST")
DB_PORT = os.getenv("PGPORT")

if not (DB_NAME and DB_USER and DB_PASS):
    raise RuntimeError(
        "Missing database credentials: ensure PGDATABASE, PGUSER, and PGPASSWORD are set"
    )

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)
conn.autocommit = True

def get_cursor():
    return conn.cursor()

if __name__ == "__main__":
    # quick smoke test
    cur = get_cursor()
    cur.execute(
      "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
    )
    print(cur.fetchall())
    cur.close()
