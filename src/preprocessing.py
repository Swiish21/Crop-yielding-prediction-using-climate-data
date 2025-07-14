import pandas as pd

def clean_data(df):
    df = df.dropna()
    # Convert categorical variables to numerical
    df = pd.get_dummies(df, columns=['Crop'], drop_first=True)
    return df