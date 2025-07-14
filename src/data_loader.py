import pandas as pd

def load_crop_data(path = ''):
    return pd.read_csv(path)

def load_climate_data(path = ''):
    return pd.read_csv(path)

def merge_datasets(crop_df, climate_df):
    return pd.merge(crop_df, climate_df, on=['Region', 'Year'])