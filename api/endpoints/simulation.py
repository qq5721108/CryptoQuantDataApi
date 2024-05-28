"""
simulation.py
Author: [Your Name]
Date: [Current Date]
Description: Simulation mode endpoints.
Iteration: init code
"""

from fastapi import APIRouter, HTTPException
from config import okx_client

router = APIRouter()

@router.post("/enable_simulation")
def enable_simulation():
    """
    启用模拟交易模式
    :return: 模拟交易模式启用信息
    """
    try:
        okx_client.enable_simulation()
        return {"message": "Simulation mode enabled"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/disable_simulation")
def disable_simulation():
    """
    禁用模拟交易模式
    :return: 模拟交易模式禁用信息
    """
    try:
        okx_client.disable_simulation()
        return {"message": "Simulation mode disabled"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
