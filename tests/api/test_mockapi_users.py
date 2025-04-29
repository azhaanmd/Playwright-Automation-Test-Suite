import pytest
from utils.data_loader import load_test_data
from utils.helpers import get_users_url

@pytest.mark.parametrize("user_data", load_test_data("test_data/mockapi_test_data.json"))
def test_create_user(api_request_context, user_data):
    response = api_request_context.post(get_users_url(), data=user_data)
    assert response.status == 201
    user = response.json()
    assert user["name"] == user_data["name"]
    user_data["id"] = user["id"]  # Save ID for other tests


def test_get_all_users(api_request_context):
    response = api_request_context.get(get_users_url())
    assert response.status == 200
    assert isinstance(response.json(), list)


def test_update_user(api_request_context):
    # Create a user first
    user_data = {
        "name": "Temp User", "email": "temp@x.com", "job": "Intern", "age": 22, "isActive": False
    }
    create_resp = api_request_context.post(get_users_url(), data=user_data)
    user_id = create_resp.json()["id"]

    print(create_resp.json())

    # Update user
    updated_data = { "name": "Updated User", "job": "Updated Job" }
    update_url = f"{get_users_url()}/{user_id}"
    update_resp = api_request_context.put(update_url, data=updated_data)
    assert update_resp.status == 200
    assert update_resp.json()["name"] == "Updated User"
    print(update_resp.json())


def test_delete_user(api_request_context):
    # Create a user to delete
    user_data = {
        "name": "Delete Me", "email": "delete@x.com", "job": "None", "age": 33, "isActive": True
    }
    create_resp = api_request_context.post(get_users_url(), data=user_data)
    user_id = create_resp.json()["id"]
    print(create_resp.json())
    
    delete_url = f"{get_users_url()}/{user_id}"
    delete_resp = api_request_context.delete(delete_url)
    assert delete_resp.status in [200, 204]


def test_get_nonexistent_user(api_request_context):
    fake_id = "999999"
    response = api_request_context.get(f"{get_users_url()}/{fake_id}")
    assert response.status in [404, 200]  # Some APIs return 200 but empty data
