#import alpaca-trade-api as tradeapi

#basic information
BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_API_KEY = "<PKR2P2YG7OH37B2271YF>"
ALPACA_SECRET_KEY = "<bF1B67k9dsfUAB3yCLE1cR64BDkVGg0MgCsdOLkq>"

#initiate rest api connection
#api = tradeapi.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, base_url=BASE_URL, api_version='v2')

#function to submit orders
#api.submit_order(symbol, qty, side(buy/sell), type(market), time_in_force(day))

ticker = 'stock the weather chose'

ticker_position = api.get_position('"ticker"')
 
price = ticker_position[market_value]
quantity = 1 / price
api.submit_order(ticker, quantity, 'buy', 'market', 'day')
