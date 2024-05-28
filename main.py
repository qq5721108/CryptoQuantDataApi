"""
main.py
Author: [Your Name]
Date: [Current Date]
Description: Entry point for the FastAPI service.
Iteration: init code
"""

from fastapi import FastAPI
from api.endpoints import market, orders, balance, simulation

app = FastAPI(
    title="CryptoQuant API",
    description="A FastAPI service for cryptocurrency quantitative trading",
    version="1.0.0"
)

# Include routers
app.include_router(market.router)
app.include_router(orders.router)
app.include_router(balance.router)
app.include_router(simulation.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the CryptoQuant API"}
