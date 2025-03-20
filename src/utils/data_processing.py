import pandas as pd
import numpy as np
from typing import Dict, List

def process_excel_file(file_path):
    # ...existing code...
    pass

def process_excel_file(file) -> pd.DataFrame:
    """
    Process uploaded Excel file and perform initial data cleaning
    """
    try:
        df = pd.read_excel(file)
        
        # Basic cleaning
        df = df.replace(['NA', 'N/A', ''], np.nan)
        
        return df
        
    except Exception as e:
        raise Exception(f"Error processing Excel file: {str(e)}")

def detect_column_types(df: pd.DataFrame) -> Dict[str, List[str]]:
    """
    Detect and categorize column types
    """
    column_types = {
        'numeric': [],
        'categorical': [],
        'datetime': [],
        'text': []
    }
    
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            column_types['numeric'].append(column)
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            column_types['datetime'].append(column)
        elif df[column].nunique() < df.shape[0] * 0.05:  # If unique values are less than 5% of total rows
            column_types['categorical'].append(column)
        else:
            column_types['text'].append(column)
            
    return column_types