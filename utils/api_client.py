# utils/api_client.py

import json
from utils.constants import REQRES_BASE_URL, ENDPOINTS
from playwright.sync_api import APIRequestContext
from utils.logger import logger
logger.debug("Logger is working fine!")
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
    logger.info("Starting registration test")
    logger.debug(f"Payload: {registration_data}")
    response = api_request_context.post(
        f"{REQRES_BASE_URL}/register", data=registration_data, headers=headers
    )
    BEARER_TOKEN.append(response.json().get('token'))
    logger.debug(f"Response status: {response.status}")
    logger.debug(f"Response body: {response.json()}")
    #IDs.append(response.json().get('id'))
    return response