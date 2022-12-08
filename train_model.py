# Import the necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, GridSearchCV, cross_val_score

def train_model(X, y):
    # Define the models to use
    models = [
        ("Linear Regression", LinearRegression()),
        ("Support Vector Regression", SVR()),
        ("Random Forest Regression", RandomForestRegressor())
    ]

    # Define the hyperparameters to search over
    hyperparameters = [
        {"fit_intercept": [True, False]},
        {"C": [0.1, 1.0, 10.0], "kernel": ["linear", "poly", "rbf"]},
        {"n_estimators": [10, 100, 1000], "max_depth": [3, 5, 7]}
    ]

    # Define the cross-validation strategy
    kf = KFold(n_splits=10, shuffle=True, random_state=1)

    # Iterate over the models and hyperparameters
    best_model = None
    best_score = 0
    for model_name, model in models:
        # Perform grid search to find the best hyperparameters
        gs = GridSearchCV(model, hyperparameters, cv=kf)
        gs.fit(X, y)

        # Evaluate the model using nested cross-validation
        scores = cross_val_score(gs, X, y, cv=kf)
        score = scores.mean()

        # Print the model and score
        print(f"{model_name}: {score:.3f}")

        # Update the best model and score
        if score > best_score:
            best_score = score
            best_model = gs

    # Return the best model
    return best_model
