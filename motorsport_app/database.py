from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

host = os.getenv("HOST")
dbname = os.getenv("DBNAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")