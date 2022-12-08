# Import the necessary modules
import get_data
import normalize_data
import train_model
import predict_price

# Get the data
data = get_data.get_data()

# Normalize the data
data = normalize_data.normalize_data(data)

# Split the data into training and testing sets
X_train = data[["time", "volume", "market_cap", "high", "low", "binance_volume", "news_sentiment"]][:int(len(data) * 0.8)]
y_train = data[["price"]][:int(len(data) * 0.8)]
X_test = data[["time", "volume", "market_cap", "high", "low", "binance_volume", "news_sentiment"]][int(len(data) * 0.8):]
y_test = data[["price"]][int(len(data) * 0.8):]

# Train the model
model = train_model.train_model(X_train, y_train)

# Make predictions on the test set
predictions = predict_price.predict_price(model, X_test)

# Print the predictions
print(predictions)
