from csv_reader import FileReader

class Startup:
    ''' Plots the cost vs revenue using matplotlib. '''

    def __init__(self):
        # Extracts the all the data from the FileReader
        file_reader = FileReader()
        self.meta_data = file_reader.meta_data
        
        # Extracts lists from the FileReader data.
        self.all_dates = self.meta_data[0]
        self.all_revenues = self.meta_data[8]
        self.all_totl_costs = self.meta_data[9]

    def organize_data(self):
        # Saving data into a per day for the year format
        daily_date = {}
        for date, revenue, cost in zip(self.all_dates,
            self.all_revenues, self.all_totl_costs):
            if date not in daily_date:
                daily_date[date] = [0.0, 0.0]
            daily_date[date][0] += revenue
            daily_date[date][1] += cost

        dates = sorted(daily_date.keys())
        revenues = [daily_date[d][0] for d in dates]
        totl_costs = [daily_date[d][1] for d in dates]

        return dates, revenues, totl_costs


