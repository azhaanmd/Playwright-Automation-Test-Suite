import pytest
from utils.db_utils import get_connection

def test_insert_user_and_fetch():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert a new user
    cursor.execute("""
        INSERT INTO users (name, email, job, age, is_active)
        VALUES (%s, %s, %s, %s, %s) RETURNING id;
    """, ("Test User", "test2@example.com", "Tester", 26, True))
    user_id = cursor.fetchone()[0]

    # Fetch the user
    cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
    user = cursor.fetchone()

    assert user[1] == "Test User"  # name
    assert user[2] == "test2@example.com"  # email
    assert user[3] == "Tester"  # job

    conn.commit()
    cursor.close()
    conn.close()



def test_fetch_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert some users
    cursor.execute("""
        INSERT INTO users (name, email, job, age, is_active)
        VALUES (%s, %s, %s, %s, %s);
    """, ("Test User 1", "test9@example.com", "Tester", 28, True))
    cursor.execute("""
        INSERT INTO users (name, email, job, age, is_active)
        VALUES (%s, %s, %s, %s, %s);
    """, ("Test User 2", "test10@example.com", "Developer", 29, True))

    # Fetch all users
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()

    assert len(users) >= 2  # We inserted two users, so we expect at least two results

    conn.commit()
    cursor.close()
    conn.close()



def test_check_user_exists():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert a new user
    cursor.execute("""
        INSERT INTO users (name, email, job, age, is_active)
        VALUES (%s, %s, %s, %s, %s) RETURNING id;
    """, ("Test User", "test7@example.com", "Tester", 30, True))
    user_id = cursor.fetchone()[0]

    # Check if the user exists
    cursor.execute("SELECT * FROM users WHERE email = %s;", ("test7@example.com",))
    user = cursor.fetchone()

    assert user is not None  # The user should exist
    assert user[2] == "test7@example.com"  # email should match

    conn.commit()
    cursor.close()
    conn.close()

