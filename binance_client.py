Import the Binance.US API client
from binance.client import Client

Set your API key and secret
client = Client(api_key="", api_secret="")

Get the trading volume for Chainlink
chainlink_volume = client.get_symbol_ticker(symbol="LINKUSDT")["volume"]

Get the trading volume for Chainlink on Binance.US
binance_data = <code to access Binance.US API and get trading volume>
