from pydantic import BaseModel

class MarketData(BaseModel):
    ticker: str
    price: float
    change: float
    previous_price: float
