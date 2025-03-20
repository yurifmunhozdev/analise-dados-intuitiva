from typing import Any, Dict
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def create_histogram(data: pd.Series, title: str) -> None:
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, alpha=0.7, color='blue')
    plt.title(title)
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def create_bar_chart(data: pd.Series, title: str) -> None:
    data.value_counts().plot(kind='bar', figsize=(10, 6), color='orange')
    plt.title(title)
    plt.xlabel('Categories')
    plt.ylabel('Counts')
    plt.xticks(rotation=45)
    plt.show()

def create_line_chart(data: pd.DataFrame, x: str, y: str, title: str) -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(data[x], data[y], marker='o')
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid()
    plt.show()

def create_scatter_plot(data: pd.DataFrame, x: str, y: str, title: str) -> None:
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x], data[y], alpha=0.5)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid()
    plt.show()

def create_correlation_heatmap(data: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 8))
    correlation = data.corr()
    sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Correlation Heatmap')
    plt.show()