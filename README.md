# Restaurant Sales Visualisation Engine
A lightweight Python app that parses transaction data to generate clean
financial charts and monthly performance metrics.

## Features
**Safe Ingestion**: Parses 10,000+ rows with missing field handlers.
**Trend Analysis**: Plots annual aggregate revenue vs. cost curves.
**Top Performers**: Finds the highest-grossing menu item per month.
**CLI Search Shell**: Interactive terminal loop for custom queries.

## 📁 File Structure
* "restaurant_data/restaurant_2024.csv" - CSV file in folder.
* "csv_reader.py" - Reads the raw CSV file and sanitizes number cells.
* "year_data.py  - Bundles total restaurant-wide data streams.
* "dish_data.py"  - Extracts unique menus and handles search logic.
* "main.py"       - **Main Hub**. Runs user loops and handles plots.

## Setup & Execution

1. Place your dataset at:
   "restaurant_data/restaurant_2024.csv"

2. Set up a virtual environment and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies:

   pip3 install matplotlib

4. Launch the dashboard hub:

   python3 main.py

## How to Use
**On Launch**: Shows unique menu items and opens a total trends chart.
**Dish Filter**: Type a dish name (e.g. "Laksa") to open its graph.
**Rankings**: Type "1" to generate monthly top performer bar charts.
**Exit**: Type "q" at the terminal prompt to close the session.
