import psycopg2
import os

def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),  # ✅ Use "db" for the service name in docker-compose
        database=os.getenv("POSTGRES_DB", "userdb"),
        user=os.getenv("POSTGRES_USER", "appuser"),
        password=os.getenv("POSTGRES_PASSWORD", "securepass")
    )

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_user(first_name, last_name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING id;", (first_name, last_name))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id

def get_user_by_id(user_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user
