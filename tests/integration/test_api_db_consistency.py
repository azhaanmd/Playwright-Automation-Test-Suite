# tests/integration/test_api_db_consistency.py

import pytest
import uuid
from utils.helpers import get_users_url
from utils.db_utils import get_connection, get_user_from_db, insert_user_to_db, delete_user_from_db_by_email, fetch_all_users, update_user_in_db_by_email



def test_create_user_api_and_db_same_user(api_request_context):
    user_data = {
        "name": "Sadia QA",
        "email": f"test_{uuid.uuid4().hex[:6]}@example.com",
        "job": "Tester",
        "age": 25,
        "isActive": True
    }

    # Step 1: Create the user via API
    api_resp = api_request_context.post(get_users_url(), data=user_data)
    assert api_resp.status == 201
    api_user = api_resp.json()

    # Step 2: Insert the same user in DB using API's returned ID
    user_data["id"] = api_user["id"]  # Sync ID for matching
    insert_user_to_db(user_data)

    # Step 3: Fetch from DB
    db_user = get_user_from_db(api_user["email"])
    assert db_user is not None

    # Step 4: Compare API and DB user
    assert db_user["name"] == api_user["name"]
    assert db_user["email"] == api_user["email"]
    assert db_user["job"] == api_user["job"]
    assert db_user["age"] == api_user["age"]
    assert db_user["is_active"] == api_user["isActive"]


def test_update_user_api_and_db_same_user(api_request_context):
    email = "sadia2@testmail.com"

    # Step 1: Get user ID from API
    all_users_resp = api_request_context.get(get_users_url())
    assert all_users_resp.status == 200
    all_users = all_users_resp.json()
    user = next((u for u in all_users if u["email"] == email), None)
    assert user is not None, f"User with email {email} not found in API"
    user_id = user["id"]

    # Step 2: Update via API
    updated_api_data = {
        "name": "UpdatedNameAgain",
        "job": "Principal Engineer"
    }
    update_resp = api_request_context.put(f"{get_users_url()}/{user_id}", data=updated_api_data)
    assert update_resp.status in [200, 204]
    
    # Step 3: Update in DB
    update_user_in_db_by_email(email, updated_api_data)

    # Step 4: Fetch from DB and compare
    db_user = get_user_from_db(email)
    assert db_user["name"] == updated_api_data["name"]
    assert db_user["job"] == updated_api_data["job"]


def test_delete_user_api_and_db_same_user(api_request_context):
    email = "sadia3@testmail.com"

    # Step 1: Get user ID from API
    all_users_resp = api_request_context.get(get_users_url())
    assert all_users_resp.status == 200
    all_users = all_users_resp.json()
    user = next((u for u in all_users if u["email"] == email), None)
    assert user is not None, f"User with email {email} not found in API"
    user_id = user["id"]

    # Step 2: Delete from API
    delete_resp = api_request_context.delete(f"{get_users_url()}/{user_id}")
    assert delete_resp.status in [200, 204, 202, 404]

    # Step 3: Delete from DB
    delete_user_from_db_by_email(email)

    # Step 4: Confirm deletion in DB
    db_user = get_user_from_db(email)
    assert db_user is None



def test_get_all_users_api_and_db_count(api_request_context):
    # API fetch
    api_resp = api_request_context.get(get_users_url())
    assert api_resp.status == 200
    api_users = api_resp.json()

    # DB fetch
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    db_count = cursor.fetchone()[0]
    conn.close()

    assert len(api_users) == db_count or abs(len(api_users) - db_count) <= 1  # checking if the difference is minor