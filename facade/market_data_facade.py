from services.market_data_service import MarketDataService

class MarketDataFacade:
    def __init__(self, tickers: list):
        self.service = MarketDataService(tickers)
    
    def get_market_data(self):
        return self.service.fetch_market_data()
