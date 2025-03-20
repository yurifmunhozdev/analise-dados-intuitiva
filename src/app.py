import streamlit as st
import pandas as pd
from utils.data_processing import process_excel_file, detect_column_types
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Relatório Empresa X",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for modern "tech" style with orange and blue colors
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #ff6600;
        color: white;
    }
    .stButton>button:hover {
        background-color: #ff8533;
    }
    .stSidebar {
        background-color: #003366;
        color: white;
    }
    .stSidebar .stButton>button {
        background-color: #ff6600;
        color: white;
    }
    .stSidebar .stButton>button:hover {
        background-color: #ff8533;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.title("📊 Relatório Empresa X")
    
    # File upload section
    uploaded_file = st.file_uploader(
        "Drop your Excel file here", 
        type=['xlsx', 'xls'],
        help="Upload an Excel file to begin analysis"
    )
    
    if uploaded_file is not None:
        try:
            # Process the uploaded file
            df = process_excel_file(uploaded_file)
            
            # Detect column types
            column_types = detect_column_types(df)
            
            # Display categorical data analysis
            st.subheader("📊 Dashboard")
            for column in column_types['categorical']:
                with st.expander(f"### {column}"):
                    fig, ax = plt.subplots()
                    df[column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
                    ax.set_ylabel('')
                    st.pyplot(fig)
            
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()
