import sqlite3
import pandas as pd


def initialize_database():

    # Read CSV dataset
    df = pd.read_csv("sales.csv")

    # Create SQLite database
    conn = sqlite3.connect("sales.db")

    # Load data into table
    df.to_sql("sales", conn, if_exists="replace", index=False)

    print("Database initialized successfully!")

    return conn


def run_query(conn, query):

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    except Exception as e:
        print("Query Error:", e)
        return None