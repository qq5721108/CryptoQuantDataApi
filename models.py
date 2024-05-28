from pydantic import BaseModel

class OrderRequest(BaseModel):
    instId: str
    side: str
    ordType: str
    sz: str
    px: str

class SimulatedAccount:
    def __init__(self):
        self.balance = {"USDT": 10000}
        self.orders = []

    def place_order(self, instId, side, ordType, sz, px):
        order = {
            "instId": instId,
            "side": side,
            "ordType": ordType,
            "sz": sz,
            "px": px,
            "status": "filled"
        }
        self.orders.append(order)
        self._update_balance(side, sz, px)
        return order

    def _update_balance(self, side, sz, px):
        if side == 'buy':
            cost = float(sz) * float(px)
            self.balance["USDT"] -= cost
        elif side == 'sell':
            revenue = float(sz) * float(px)
            self.balance["USDT"] += revenue

    def get_balance(self):
        return self.balance
