import streamlit as st
import pandas as pd
from utils.data_processing import load_data, summarize_data
from components.visualizations import plot_histogram, plot_bar_chart, plot_line_chart

def main():
    st.title("Excel Data Analysis Web Application")
    
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
    
    if uploaded_file is not None:
        # Load data
        data = load_data(uploaded_file)
        
        # Display data summary
        st.subheader("Data Summary")
        summary = summarize_data(data)
        st.write(summary)
        
        # Visualization options
        st.subheader("Visualizations")
        visualization_type = st.selectbox("Select a visualization type", 
                                           ["Histogram", "Bar Chart", "Line Chart"])
        
        if visualization_type == "Histogram":
            column = st.selectbox("Select a column for histogram", data.columns)
            plot_histogram(data[column])
        
        elif visualization_type == "Bar Chart":
            column = st.selectbox("Select a column for bar chart", data.columns)
            plot_bar_chart(data[column])
        
        elif visualization_type == "Line Chart":
            x_column = st.selectbox("Select x-axis column", data.columns)
            y_column = st.selectbox("Select y-axis column", data.columns)
            plot_line_chart(data[x_column], data[y_column])

if __name__ == "__main__":
    main()