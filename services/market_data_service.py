import yfinance as yf

class MarketDataService:
    def __init__(self):
        self.tickers = ["BTC-USD", "ETH-USD", "PETR4.SA"]

    def fetch_market_data(self, period):
        data = {}
        for ticker in self.tickers:
            try:
                ticker_data = yf.Ticker(ticker).history(period=period)
                if not ticker_data.empty:
                    current_price = ticker_data['Close'].iloc[-1]
                    previous_price = ticker_data['Close'].iloc[-2]
                    change = (current_price - previous_price) / previous_price
                    data[ticker] = {
                        "price": current_price,
                        "change": change,
                        "previous_price": previous_price
                    }
                else:
                    print(f"No data for ticker {ticker}")
            except Exception as e:
                print(f"Error fetching data for {ticker}: {e}")
        return data
