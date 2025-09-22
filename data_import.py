# data_import.py
# Read CSVs from datasets/ and write to DB using pandas.to_sql
import os
import pandas as pd
from sqlalchemy import create_engine
from config import DB_URL, DATASET_FOLDER

CSV_FILES = [
    ("drivers.csv", "drivers"),
    ("constructors.csv", "constructors"),
    ("races.csv", "races"),
    ("results.csv", "results"),
    ("lap_times.csv", "lap_times"),
    # add other relevant csvs if present
]

def load_csvs_to_db():
    engine = create_engine(DB_URL)
    os.makedirs(DATASET_FOLDER, exist_ok=True)
    for csvname, tablename in CSV_FILES:
        path = os.path.join(DATASET_FOLDER, csvname)
        if not os.path.exists(path):
            print(f"Warning: {path} not found. Skipping {tablename}.")
            continue
        print(f"Loading {path} -> table {tablename} ...")
        df = pd.read_csv(path)
        # Basic cleanup: lower column names
        df.columns = [c.strip() for c in df.columns]
        df.to_sql(tablename, engine, if_exists="replace", index=False)
        print(f"Loaded {len(df):,} rows into {tablename}.")
    print("All available CSVs imported.")

if __name__ == "__main__":
    load_csvs_to_db()
