# Import necessary library for data manipulation
import pandas as pd

# Define a function to load crop data from a CSV file
def load_crop_data(path='data/raw/crop_yield.csv'):
    """
    Load crop data from a CSV file.

    Parameters:
    path (str): Path to the CSV file (optional, defaults to an empty string)

    Returns:
    df (pandas DataFrame): Loaded crop data
    """
    # Read the CSV file into a pandas DataFrame
    return pd.read_csv(path)

# Define a function to load climate data from a CSV file
def load_climate_data(path='data/raw/climate_data.csv'):
    """
    Load climate data from a CSV file.

    Parameters:
    path (str): Path to the CSV file (optional, defaults to an empty string)

    Returns:
    df (pandas DataFrame): Loaded climate data
    """
    # Read the CSV file into a pandas DataFrame
    return pd.read_csv(path)

# Define a function to merge crop and climate data on common columns
def merge_datasets(crop_df, climate_df):
    """
    Merge crop and climate data on common columns.

    Parameters:
    crop_df (pandas DataFrame): Crop data
    climate_df (pandas DataFrame): Climate data

    Returns:
    df (pandas DataFrame): Merged crop and climate data
    """
    # Merge the two DataFrames on the 'Region' and 'Year' columns
    return pd.merge(crop_df, climate_df, on=['Region', 'Year'])