# db_create.py
# Creates/cleans the SQLite DB file (f1.db)
from sqlalchemy import create_engine
from config import DB_URL
import os

def recreate_db():
    # For SQLite file remove it if exists
    if DB_URL.startswith("sqlite:///"):
        path = DB_URL.replace("sqlite:///", "")
        if os.path.exists(path):
            os.remove(path)
            print(f"Removed existing DB file: {path}")
    engine = create_engine(DB_URL)
    # engine will create the file on first write
    print("Database will be created on first write.")
    return engine

if __name__ == "__main__":
    recreate_db()
    print("DB creation script finished. Next: data_import.py")
