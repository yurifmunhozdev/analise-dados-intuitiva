import pandas as pd

def process_excel_file(file):
    """
    Process an uploaded Excel file and return a pandas DataFrame.
    
    Args:
        file: The uploaded file object or file path
    Returns:
        pd.DataFrame: The processed DataFrame
    """
    try:
        df = pd.read_excel(file)
        # Add your data processing logic here
        return df
    except Exception as e:
        raise Exception(f"Error processing Excel file: {str(e)}")
