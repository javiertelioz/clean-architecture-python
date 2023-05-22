import os
from unittest.mock import patch

import pytest
import requests
from app.domain.contracts.transactional.transaction_client import TransactionClient
from app.infrastructure.services.pipedream_api_service import PipedreamApi


@pytest.fixture
def mocked_requests_post():
    with patch("requests.post") as mock_post:
        yield mock_post


def test_pipedream_api_missing_env_variable():
    original_env_value = os.getenv("PIPEDREAM_API_ENDPOINT")

    os.environ["PIPEDREAM_API_ENDPOINT"] = ""

    with pytest.raises(ValueError):
        PipedreamApi()

    os.environ["PIPEDREAM_API_ENDPOINT"] = original_env_value


def test_get_transactions(mocked_requests_post):
    response_data = {
        "transaction_id": 7625323047,
        "user_id": 1001,
        "transaction_type": "debit",
        "amount": 96305,
        "description": "Transaction 1",
        "datetime": "2023-03-07T07:44:55",
    }

    mocked_requests_post.return_value.json.return_value = response_data
    mocked_requests_post.return_value.raise_for_status.return_value = None

    pipedream_api = PipedreamApi()

    transactions = pipedream_api.get_transactions("2023-05-19")

    assert transactions == response_data

    mocked_requests_post.assert_called_once_with(
        pipedream_api.api_url, json={"date": "2023-05-19"}, headers={"Content-Type": "application/json"}
    )


def test_pipedream_api_empty_response(mocked_requests_post):
    response_data = []
    mocked_requests_post.return_value.json.return_value = response_data
    mocked_requests_post.return_value.raise_for_status.return_value = None

    pipedream_api = PipedreamApi()

    transactions = pipedream_api.get_transactions("2023-05-19")

    assert transactions == response_data

    mocked_requests_post.assert_called_once_with(
        pipedream_api.api_url, json={"date": "2023-05-19"}, headers={"Content-Type": "application/json"}
    )


def test_pipedream_api_error_response(mocked_requests_post):
    error_message = "Internal Server Error"
    mocked_requests_post.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError(error_message)

    pipedream_api = PipedreamApi()

    with pytest.raises(requests.exceptions.HTTPError) as exc_info:
        pipedream_api.get_transactions("2023-05-19")

    assert str(exc_info.value) == error_message

    mocked_requests_post.assert_called_once_with(
        pipedream_api.api_url, json={"date": "2023-05-19"}, headers={"Content-Type": "application/json"}
    )
