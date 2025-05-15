from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

host = os.getenv("HOST")
dbname = os.getenv("DBNAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")

def get_connection():
    return psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)

def init_database():
    with open("schema.sql", "r") as file:
        schema = file.read()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(schema)
            conn.commit()