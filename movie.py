import psycopg2
import csv

# Database connection details
DB_NAME = "my_test_db"
DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_PORT = "5432"

# CSV file path
CSV_FILE_PATH = "data/movie.csv"

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

# Ensure the table exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        movieID SERIAL PRIMARY KEY,
        title TEXT
    );
""")
conn.commit()

# Read and insert data from CSV
with open(CSV_FILE_PATH, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip header row if present

    for idx, row in enumerate(csv_reader, start=1):
        cur.execute(
            "INSERT INTO movies (movieID, title) VALUES (%s, %s)",
            (row[0], row[1])
        )
        if idx % 10000 == 0:  # Commit every 10,000 rows
            conn.commit()
            print(f"Inserted {idx} rows...")

# Final commit and cleanup
conn.commit()
cur.close()
conn.close()

print("Data import completed successfully!")
