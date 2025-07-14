# Import necessary library for data manipulation
import pandas as pd

# Define a function to clean and preprocess the data
def clean_data(df):
    """
    Clean and preprocess the data by removing missing values and converting categorical variables to numerical.

    Parameters:
    df (pandas DataFrame): Data to be cleaned and preprocessed

    Returns:
    df (pandas DataFrame): Cleaned and preprocessed data
    """
    # Remove rows with missing values
    df = df.dropna()

    # Convert categorical variables to numerical using one-hot encoding
    # The 'Crop' column is converted to numerical, and the first category is dropped to avoid multicollinearity
    df = pd.get_dummies(df, columns=['Crop'], drop_first=True)

    # Return the cleaned and preprocessed data
    return df