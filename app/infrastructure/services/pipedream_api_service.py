import os

import requests
from app.domain.contracts.transactional.transaction_client import TransactionClient


class PipedreamApi(TransactionClient):
    def __init__(self):
        self.api_url = os.getenv("PIPEDREAM_API_ENDPOINT")

        if not self.api_url:
            raise ValueError("Missing PIPEDREAM_API_ENDPOINT environment variable")

    def get_transactions(self, date):
        url = self.api_url
        headers = {"Content-Type": "application/json"}
        payload = {"date": date}

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        return response.json()
