# Import necessary libraries for machine learning and data processing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Define a function to train a linear regression model on a given dataset
def train_model(df):
    """
    Train a linear regression model on a dataset to predict crop yield.

    Parameters:
    df (pandas DataFrame): Dataset containing features and target variable 'Yield'

    Returns:
    model (LinearRegression): Trained linear regression model
    """
    # Split the dataset into features (X) and target variable (y)
    X = df.drop(['Yield', 'Region', 'Year'], axis=1)  # Features: all columns except 'Yield', 'Region', and 'Year'
    y = df['Yield']  # Target variable: 'Yield'

    # Split the data into training and testing sets (80% for training and 20% for testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)  # Train the model on the training data

    # Make predictions on the testing data
    y_pred = model.predict(X_test)

    # Evaluate the model's performance using Root Mean Squared Error (RMSE) and R-squared (R2)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)

    # Print the model's performance metrics
    print(f"RMSE: {rmse:.2f}")
    print(f"R^2: {r2:.2f}")

    # Save the trained model to a file
    joblib.dump(model, 'models/crop_yield_model.pkl')

    # Return the trained model
    return model