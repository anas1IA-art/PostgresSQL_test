import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cur = conn.cursor()

# Insert large data
for i in range(1, 1000):  # 1 million rows
    email = f"user{i}@example.com"
    cur.execute(
        """
        INSERT INTO users (name, email, age)
        VALUES (%s, %s, %s)
        ON CONFLICT (email) DO NOTHING;
        """,
        (f"User_{i}", email, i % 100)
    )
    if i % 10000 == 0:  # Commit every 10,000 rows
        conn.commit()
        print(f"Inserted {i} rows...")

# Final commit and cleanup
conn.commit()
cur.close()
conn.close()