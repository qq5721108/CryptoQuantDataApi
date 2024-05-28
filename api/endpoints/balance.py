"""
balance.py
Author: [Your Name]
Date: [Current Date]
Description: Balance endpoints.
Iteration: init code
"""

from fastapi import APIRouter, HTTPException
from config import okx_client

router = APIRouter()

@router.get("/balance")
def get_balance():
    """
    获取账户余额
    :return: 账户余额
    """
    try:
        balance = okx_client.get_account_balance()
        return balance
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
