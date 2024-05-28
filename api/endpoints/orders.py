"""
orders.py
Author: [Your Name]
Date: [Current Date]
Description: Order management endpoints.
Iteration: init code
"""

from fastapi import APIRouter, HTTPException
from config import okx_client
from models.order_request import OrderRequest

router = APIRouter()

@router.post("/order")
def place_order(order: OrderRequest):
    """
    下单
    :param order: 订单请求
    :return: 下单结果
    """
    try:
        result = okx_client.place_order(
            instId=order.instId,
            side=order.side,
            ordType=order.ordType,
            sz=order.sz,
            px=order.px
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
