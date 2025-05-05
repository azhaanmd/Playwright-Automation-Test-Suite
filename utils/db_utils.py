

import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

def get_connection():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("DATABASE_URL not found in .env file.")
    return psycopg2.connect(db_url)

def fetch_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def insert_user(name, email, job, age, is_active):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO users (name, email, job, age, is_active)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, email, job, age, is_active))
    conn.commit()
    cursor.close()
    conn.close()



def get_user_from_db(user_email):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM users WHERE email LIKE %s", (f"%{user_email}%",))
    db_user = cursor.fetchone()
    conn.close()
    return db_user


def insert_user_to_db(user_data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO users (name, email, job, age, is_active)
        VALUES (%s, %s, %s, %s, %s) RETURNING id
        """,
        (user_data["name"], user_data["email"], user_data["job"], user_data["age"], user_data["isActive"])
    )
    user_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return user_id


def update_user_in_db_by_email(email, updated_data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE users SET name = %s, job = %s WHERE email = %s
        """,
        (updated_data["name"], updated_data["job"], email)
    )
    conn.commit()
    conn.close()



def delete_user_from_db_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE email = %s", (email,))
    conn.commit()
    conn.close()