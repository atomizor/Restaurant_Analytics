import matplotlib.pyplot as plt
from csv_reader import FileReader

class DishData:
    ''' Plots the cost vs revenue using matplotlib. '''

    def __init__(self):
        # Extracts the all the data from the FileReader
        file_reader = FileReader()
        self.meta_data = file_reader.meta_data   

        # Lists extracted from file_reader
        self.all_dates = self.meta_data[0]
        self.all_revenues = self.meta_data[8]
        self.all_totl_costs = self.meta_data[9]
        self.all_qtys = self.meta_data[7]
        self.all_dishes = self.meta_data[1]

    def get_dish_name(self):
        ''' Extracts the name of the manu items in the csv file '''

        menu_item = self.meta_data[1]

        dish_data = {}
        for item in menu_item:
            if item not in dish_data:
                dish_data[item] = "None"
        print("\n********* CSV Analytics **********\n")
        print("\n** Names of Dishes on the Menu **\n")
        dish_list = []
        for dish in dish_data:
            print(f"{dish}")
            dish_list.append(dish)
        return dish_list

    def ask_find_helper(self, ask):
        # A copy of the self.organize_data() from dish_data with mods  
        # Cleanly saves the total data of a day into correct date

        daily_date = {}
        for date, revenue, cost, dish in zip(self.all_dates,
            self.all_revenues, self.all_totl_costs,
            self.all_dishes):
            if date not in daily_date:
                daily_date[date] = [0.0, 0.0]
            if ask == dish:
                daily_date[date][0] += (revenue)
                daily_date[date][1] += (cost)

        dates = sorted(daily_date.keys())
        revenues = [daily_date[d][0] for d in dates]
        totl_costs = [daily_date[d][1] for d in dates]

        return dates, revenues, totl_costs

    def top_dish_monthly(self):
    # Performs calculations and stores data for Top Dish per month
        months, dishes, highest_revs = [], [], []

        monthly_sales = {}

        for date, dish, rev in zip(
            self.all_dates,
            self.all_dishes,
            self.all_revenues
        ):
            month_name = date.strftime('%B')

            if month_name not in monthly_sales:
                monthly_sales[month_name] = {}

            if not dish in monthly_sales[month_name]:
                monthly_sales[month_name][dish] = 0

            monthly_sales[month_name][dish] += (rev)

        # Loop through the dishes in each month to find the top dishes
        for month in monthly_sales:
            dish_count = monthly_sales[month]

            highest_rev = 0
            best_dish = "No Data"

            for dish in dish_count:
                if dish_count[dish] > highest_rev:
                    highest_rev = dish_count[dish]
                    best_dish = dish
            months.append(month)
            dishes.append(dish)
            highest_revs.append(highest_rev)

        return months, dishes, highest_revs

                    

    

            