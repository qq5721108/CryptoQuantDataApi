"""
order_request.py
Author: [Your Name]
Date: [Current Date]
Description: Data model for order requests.
Iteration: init code
"""

from pydantic import BaseModel

class OrderRequest(BaseModel):
    instId: str  # 交易对，例如 "BTC-USDT"
    side: str  # 买卖方向，例如 "buy" 或 "sell"
    ordType: str  # 订单类型，例如 "market" 或 "limit"
    sz: str  # 交易数量
    px: str = None  # 订单价格，限价单需要
