from fastapi import FastAPI
from routers.market_data_router import router as market_data_router

app = FastAPI()

app.include_router(market_data_router)
