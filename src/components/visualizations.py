import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.data_processing import detect_column_types

def generate_visualizations(df):
    """
    Generate appropriate visualizations based on data types
    """
    column_types = detect_column_types(df)
    
    # Numeric visualizations
    if column_types['numeric']:
        st.subheader("📈 Numeric Analysis")
        
        # Correlation heatmap for numeric columns
        if len(column_types['numeric']) > 1:
            st.write("#### Correlation Matrix")
            correlation = df[column_types['numeric']].corr()
            fig = px.imshow(correlation, 
                          text=correlation.round(2),
                          aspect="auto",
                          color_continuous_scale="RdBu")
            st.plotly_chart(fig, use_container_width=True)
        
        # Distribution plots for numeric columns
        st.write("#### Distribution Plots")
        for col in column_types['numeric']:
            fig = px.histogram(df, x=col, title=f"Distribution of {col}")
            st.plotly_chart(fig, use_container_width=True)
    
    # Categorical visualizations
    if column_types['categorical']:
        st.subheader("📊 Categorical Analysis")
        for col in column_types['categorical']:
            value_counts = df[col].value_counts()
            fig = px.pie(values=value_counts.values, 
                        names=value_counts.index, 
                        title=f"Distribution of {col}")
            st.plotly_chart(fig, use_container_width=True)
    
    # Time series visualizations
    if column_types['datetime']:
        st.subheader("⏰ Time Series Analysis")
        for date_col in column_types['datetime']:
            for num_col in column_types['numeric']:
                fig = px.line(df, 
                            x=date_col, 
                            y=num_col,
                            title=f"{num_col} over time")
                st.plotly_chart(fig, use_container_width=True)