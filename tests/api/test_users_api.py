import pytest
from utils.api_client import create_user, get_user, register_user  # Make sure to import register_user
from utils.data_loader import load_test_data  # Assuming this function loads JSON data
from utils.constants import REQRES_BASE_URL
IDs = []
user_count = 1

@pytest.mark.parametrize("registration_data", load_test_data("test_data/users_test_data.json"))
def test_register_user(api_request_context, registration_data):
    register_response = register_user(api_request_context, registration_data)
    assert register_response.status == 200, f"Got Response: {register_response.status}"
    register_data = register_response.json()
    print(register_data)
    token = register_data.get('token')
    assert token is not None, "Token is None"
   


@pytest.mark.parametrize("user_data", load_test_data("test_data/users_test_data.json"))
def test_create_user(api_request_context, user_data):
    # Use the user data to create a new user (no token needed here)
    create_response = create_user(api_request_context, user_data)
    assert create_response.status == 201, f"Got Response: {create_response.status}"
    create_data = create_response.json()
    created_user_id = create_data.get("id")
    assert created_user_id is not None, "User ID is None"
    IDs.append(created_user_id)
    print(f"Created User ID: {created_user_id}")


@pytest.mark.parametrize("user_data", load_test_data("test_data/users_test_data.json"))
def test_get_user(api_request_context, user_data):
    global user_count
    get_response = get_user(api_request_context, user_count)
    user_count+=1
    assert get_response.status == 200, f"Got Response: {get_response.status}"
    fetched_data = get_response.json()
    print(f"Fetched User Data: {fetched_data}")