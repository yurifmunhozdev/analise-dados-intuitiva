# Streamlit Excel Analysis

This project is a simple web application built using Streamlit that allows users to upload Excel files for data analysis and visualization. The application provides various functionalities to process the uploaded data and generate insightful visualizations.

## Features

- Upload Excel files for analysis.
- Automatic detection of data types and summary statistics.
- Visualizations including histograms, bar charts, line charts, scatter plots, and correlation heatmaps.
- User-friendly interface for easy interaction.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-excel-analysis
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command in your terminal:
```
streamlit run src/app.py
```

Once the application is running, you can access it in your web browser at `http://localhost:8501`.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.