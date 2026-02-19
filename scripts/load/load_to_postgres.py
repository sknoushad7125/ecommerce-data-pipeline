import psycopg2
import csv
import os

conn = psycopg2.connect(
    dbname="ecommerce_dw",
    user="shaik.noushad",
    password="",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

processed_path = "data/processed/orders"

for file in os.listdir(processed_path):
    if file.endswith(".csv"):
        with open(os.path.join(processed_path, file), "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                cur.execute(
                    """
                    INSERT INTO fact_orders
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                    """,
                    row
                )

conn.commit()
cur.close()
conn.close()

print("Data loaded into PostgreSQL")

