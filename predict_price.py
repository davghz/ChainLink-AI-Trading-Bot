# Import the necessary modules
import pandas as pd

def predict_price(model, X):
    # Make predictions using the model
    y_pred = model.predict(X)

    # Convert the predictions to a DataFrame
    predictions = pd.DataFrame(y_pred, columns=["price"])

    # Return the predictions
    return predictions
