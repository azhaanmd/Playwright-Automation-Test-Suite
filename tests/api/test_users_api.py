import pytest
from utils.api_client import create_user, get_user, register_user  # Make sure to import register_user
from utils.data_loader import load_test_data  # Assuming this function loads JSON data
from utils.constants import REQRES_BASE_URL
from utils.logger import logger
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



#advanced API Test Cases

# @pytest.mark.parametrize("user_data", load_test_data("test_data/invalid_user_data.json"))
# def test_create_user_with_invalid_data(api_request_context, user_data):
#     # Step 1: Try to create a user with invalid data
#     create_response = create_user(api_request_context, user_data)
#     print(create_response.json())
#     # Step 2: Assert that the response status is 400 (Bad Request)
#     print(f"Create User Response: {create_response.text}")  # Print the response text for debugging
#     print(f"Create User Status: {create_response.status}")  # Print the response status code
#     assert create_response.status == 400, f"Expected status code 400, but got {create_response.status}"

#     # Step 3: Validate that the error message is as expected
#     error_data = create_response.json()  # Assuming the response returns a JSON with an error message
#     assert "error" in error_data, f"Error message not found in response: {create_response.text}"
#     print(f"Error Message: {error_data['error']}")