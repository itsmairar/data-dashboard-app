from fastapi import APIRouter
from services.market_data_service import MarketDataService

router = APIRouter()

@router.get("/market-data/")
async def get_market_data(period: str):
    service = MarketDataService()
    data = service.fetch_market_data(period)
    return data
