"""
okx_api.py
Author: [Your Name]
Date: [Current Date]
Description: OKX API client service.
Iteration: init code
"""

import requests

class OKXClient:
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
        self.base_url = "https://www.okx.com"
        self.simulation_mode = False

    def _create_headers(self):
        return {
            "OK-ACCESS-KEY": self.api_key,
            "OK-ACCESS-SIGN": self.secret_key,
            "OK-ACCESS-TIMESTAMP": "timestamp",  # 应该动态生成
            "OK-ACCESS-PASSPHRASE": self.passphrase
        }

    def get_account_balance(self):
        endpoint = "/api/v5/account/balance"
        headers = self._create_headers()
        response = requests.get(self.base_url + endpoint, headers=headers)
        return response.json()

    def place_order(self, instId, side, ordType, sz, px=None):
        if self.simulation_mode:
            return {"message": "Simulation mode active, order not placed."}

        endpoint = "/api/v5/trade/order"
        headers = self._create_headers()
        data = {
            "instId": instId,
            "side": side,
            "ordType": ordType,
            "sz": sz,
        }
        if px:
            data["px"] = px
        response = requests.post(self.base_url + endpoint, headers=headers, json=data)
        return response.json()

    def get_market_data(self, instId):
        endpoint = f"/api/v5/market/ticker?instId={instId}"
        headers = self._create_headers()
        response = requests.get(self.base_url + endpoint, headers=headers)
        return response.json()

    def enable_simulation(self):
        self.simulation_mode = True

    def disable_simulation(self):
        self.simulation_mode = False
