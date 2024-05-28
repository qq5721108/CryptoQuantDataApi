"""
market.py
Author: [Your Name]
Date: [Current Date]
Description: Market data endpoints.
Iteration: init code
"""

from fastapi import APIRouter, HTTPException
from config import okx_client

router = APIRouter()

@router.get("/market/{instId}")
def get_market_data(instId: str):
    """
    获取市场数据
    :param instId: 交易对 ID
    :return: 市场数据
    """
    try:
        market_data = okx_client.get_market_data(instId)
        return market_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
