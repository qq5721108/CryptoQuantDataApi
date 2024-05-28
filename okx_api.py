import requests
import time
import hmac
import hashlib
import base64
from typing import Dict
import json


class OKXClient:
    def __init__(self, api_key: str, secret_key: str, passphrase: str = None):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
        self.base_url = "https://www.okx.com"
        self.simulation_mode = False
        self.simulated_balance = {"USDT": 10000}
        self.simulated_orders = []

    def enable_simulation(self):
        self.simulation_mode = True

    def disable_simulation(self):
        self.simulation_mode = False

    def _sign(self, timestamp: str, method: str, request_path: str, body: str = '') -> str:
        message = f'{timestamp}{method}{request_path}{body}'
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message.encode('utf-8'), hashlib.sha256).digest()
        return base64.b64encode(signature).decode()

    def _get_headers(self, method: str, request_path: str, body: str = '') -> Dict[str, str]:
        timestamp = str(time.time())
        headers = {
            'OK-ACCESS-KEY': self.api_key,
            'OK-ACCESS-SIGN': self._sign(timestamp, method, request_path, body),
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-PASSPHRASE': self.passphrase if self.passphrase else '',
            'Content-Type': 'application/json'
        }
        return headers

    def get_account_balance(self):
        if self.simulation_mode:
            return self.simulated_balance
        method = 'GET'
        request_path = '/api/v5/account/balance'
        headers = self._get_headers(method, request_path)
        response = requests.get(self.base_url + request_path, headers=headers)
        return response.json()

    def place_order(self, instId: str, side: str, ordType: str, sz: str, px: str):
        if self.simulation_mode:
            order = {
                "instId": instId,
                "side": side,
                "ordType": ordType,
                "sz": sz,
                "px": px,
                "status": "filled"
            }
            self.simulated_orders.append(order)
            # Adjust balance based on the order
            if side == 'buy':
                cost = float(sz) * float(px)
                self.simulated_balance["USDT"] -= cost
            else:
                self.simulated_balance["USDT"] += float(sz) * float(px)
            return order
        method = 'POST'
        request_path = '/api/v5/trade/order'
        body = {
            "instId": instId,
            "side": side,
            "ordType": ordType,
            "sz": sz,
            "px": px
        }
        body_json = json.dumps(body)
        headers = self._get_headers(method, request_path, body_json)
        response = requests.post(self.base_url + request_path, headers=headers, json=body)
        return response.json()

    def get_market_data(self, instId: str):
        method = 'GET'
        request_path = f'/api/v5/market/ticker?instId={instId}'
        headers = self._get_headers(method, request_path)
        response = requests.get(self.base_url + request_path, headers=headers)
        return response.json()
