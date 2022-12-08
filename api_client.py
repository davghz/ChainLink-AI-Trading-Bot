import coinbase
from coinbase.wallet.client import Client

Set your API key and secret
client = Client(api_key="", api_secret="")

Get the market data for Chainlink from Coinbase
data = client.get_historic_prices("LINK-USD")
