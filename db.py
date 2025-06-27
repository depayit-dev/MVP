import psycopg2
import os

def get_db():
    try:
        return psycopg2.connect(os.environ.get("DATABASE_URL"))
    except Exception as e:
        raise Exception("Database connection failed: " + str(e))