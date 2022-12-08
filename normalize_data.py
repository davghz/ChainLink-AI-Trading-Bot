# Import the necessary modules
import pandas as pd

def normalize_data(data):
    # Normalize the data
    data["price"] = (data["price"] - data["price"].mean()) / data["price"].std()
    data["volume"] = (data["volume"] - data["volume"].mean()) / data["volume"].std()
    data["market_cap"] = (data["market_cap"] - data["market_cap"].mean()) / data["market_cap"].std()
    data["high"] = (data["high"] - data["high"].mean()) / data["high"].std()
    data["low"] = (data["low"] - data["low"].mean()) / data["low"].std()
    data["binance_volume"] = (data["binance_volume"] - data["binance_volume"].mean()) / data["binance_volume"].std()
    data["news_sentiment"] = (data["news_sentiment"] - data["newsiment"].mean()) / data["news_sentiment"].std()

    # Return the normalized data
    return data
