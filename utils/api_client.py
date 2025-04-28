# utils/api_client.py

import json
from utils.constants import REQRES_BASE_URL, ENDPOINTS
from playwright.sync_api import APIRequestContext

BEARER_TOKEN = []

def create_user(api_request_context, user_data):
    # Send POST request to create a user
    headers = {"x-api-key": "reqres-free-v1"}
    response = api_request_context.post(
        f"{REQRES_BASE_URL}/users", data=user_data, headers=headers
    )
    return response


def get_user(api_request_context, user_id):
    # Send GET request to fetch a user
    headers = {"x-api-key": "reqres-free-v1"}
    response = api_request_context.get(
        f"{REQRES_BASE_URL}/users/{user_id}", headers=headers
        )
    return response


def register_user(api_request_context, registration_data):
    # Send POST request to register a user and get a token
    headers = {"x-api-key": "reqres-free-v1"}
    response = api_request_context.post(
        f"{REQRES_BASE_URL}/register", data=registration_data, headers=headers
    )
    BEARER_TOKEN.append(response.json().get('token'))
    #IDs.append(response.json().get('id'))
    return response