import matplotlib.pyplot as plt
from year_data import Startup
from dish_data import DishData
from csv_reader import FileReader
import sys

class PlotMain:
    ''' Main Program - Runs the loops and plots the data '''

    def __init__(self):
        self.startup = Startup()
        self.dishdata = DishData()
        file_reader = FileReader()
        self.meta_data = file_reader.meta_data

    def main_loop(self):
        ''' Chart when the program starts up and dish names displayed '''

        self.dishdata.get_dish_name()
        (self.dates,
        self.revenues,
        self.totl_costs) = self.startup.organize_data()
        self.plot_chart()

        while True:
            print("\nEnter the name of the dish for yearly data")
            print("Enter '1' to get top performers of each month for 2024")
            ask = input("['q' to quit]: ").strip().title()
            
            if ask == 'Q':
                sys.exit()

            elif ask == '1':
                self.best_dishes_permonth()

            elif ask in self.meta_data[1]:
                self.ask = ask
                (self.dates,
                self.revenues,
                self.totl_costs) = self.dishdata.ask_find_helper(ask)
                self.plot_chart(title_name=ask)

            else:
                print("\n! Dish not found in records !\n")
    
    def plot_chart(self, title_name="All Dishes"):

        # Plotting the chart from dish_data.py and year_data.py

        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots(figsize=(15, 8))
        ax.plot(self.dates, self.revenues, color='green', alpha=0.5)
        ax.plot(self.dates, self.totl_costs, color='red', alpha=0.5)
        ax.fill_between(self.dates, self.revenues,
        self.totl_costs, facecolor='green', alpha=0.1)
        
        ax.set_title(f"Revenue Vs. Cost - Data for {title_name}",
            fontsize=28)
        ax.set_xlabel("", fontsize=16)
        fig.autofmt_xdate()
        ax.set_ylabel("Amounts in U.S Dollars ($)", fontsize=16)

        # Formats (;,) the numbers on y-axis 
        ax.yaxis.set_major_formatter('${x:,.0f}')
        ax.tick_params(labelsize=10)

        plt.show()

    def best_dishes_permonth(self):
        # Exclusive chart for Top Dish each month's data
        months, dishes, highest_revs = self.dishdata.top_dish_monthly()

        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots(figsize=(15, 8))
        ax.bar(months, highest_revs, color='royalblue', alpha=0.5)

                # Name of dish on top of the bar
        for idx, (dish, rev) in enumerate(zip(dishes, highest_revs)):
            ax.text(idx, rev + (max(highest_revs) * 0.01), dish,
                ha='center', va='bottom', fontsize=10, weight='bold')
        
        ax.set_title(f"Top Perforiming Dishes Per Month (Revenue)",
            fontsize=28)
        ax.set_xlabel("", fontsize=16)
        fig.autofmt_xdate()

        ax.set_ylabel("Amounts in U.S Dollars ($)", fontsize=16)

        # Formats (;,) the numbers on y-axis 
        ax.yaxis.set_major_formatter('${x:,.0f}')
        ax.tick_params(labelsize=10)

        plt.show()

if __name__ == "__main__":
    program = PlotMain()
    program.main_loop()


