import pandas as pd

def read_excel(file):
    return pd.read_excel(file)

def detect_data_types(df):
    return df.dtypes

def summarize_data(df):
    return df.describe()

def handle_missing_values(df):
    return df.fillna(method='ffill')

def basic_statistical_analysis(df):
    return {
        'mean': df.mean(),
        'median': df.median(),
        'std_dev': df.std(),
        'min': df.min(),
        'max': df.max()
    }