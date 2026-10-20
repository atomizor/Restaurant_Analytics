from pathlib import Path
import csv
from datetime import datetime

class FileReader:
    ''' Reads and loads csv file data into lists '''

    def __init__(self):
        # Saved data stored here after reading the csv file

        self.data_rows = self.csv_reader()
        self.meta_data = self.list_data()


    def csv_reader(self):
        # Functions that reads data from the csv file.

        path = Path('restaurant_data/restaurant_2024.csv')
        lines = path.read_text().splitlines()

        reader = csv.DictReader(lines)
        header_row = next(reader)

        return list(reader)

    def list_data(self):
        # Functions that stores data from the csv file in lists.
        
        dates, dishes, rest_types, meal_types = [], [], [], []
        costs, mkt_prices, prices, qtys_sold = [], [], [], []
        revenues, totl_costs, differences, weathers = [], [], [], []

        for row in self.data_rows:
            date_str = row.get('date', '01/01/2024')
            date = datetime.strptime(date_str, '%m/%d/%Y')
            
            dish = row.get('menu_item_name', 'Unknown')
            rest_type = row.get('restaurant_type', 'Unknown')
            meal_type = row.get('meal_type', 'Unknown')
            weather = row.get('weather_condition', 'Unknown')
            
            cost = float(row.get('typical_ingredient_cost') or 0.0)
            mkt_price = float(row.get('observed_market_price') or 0.0)
            price = float(row.get('actual_selling_price') or 0.0)
            qty_sold = int(row.get('quantity_sold') or 0)

            dates.append(date)
            dishes.append(dish)
            rest_types.append(rest_type)
            meal_types.append(meal_type)
            costs.append(cost)
            mkt_prices.append(mkt_price)
            prices.append(price)
            qtys_sold.append(qty_sold)
            weathers.append(weather)

            # Further Calculations, total revenues and costs calculated
            revenue = (price*qty_sold)
            totl_cost = (cost*qty_sold)
            difference = ((price - mkt_price)/ 100)

            revenues.append(revenue)
            totl_costs.append(totl_cost)
            differences.append(difference)

        meta_data = (
            dates, dishes, rest_types, meal_types,
            costs, mkt_prices, prices, qtys_sold,
            revenues, totl_costs, differences, weathers
        )

        return meta_data