import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data import Data

class Visual(Data):
    def __init__(self, link) -> None:
        super().__init__(link)

    def time_series(self, mv=20, date_range="all"):
        stock_data = self.df.copy()
        stock_data[f'{mv}-day SMA'] = stock_data['Previous'].rolling(window=mv).mean()

        # Filter data based on the date_range
        today = pd.Timestamp.now()

        if date_range == 'year':
            start_date = today - pd.DateOffset(years=1)
        elif date_range == 'week':
            start_date = today - pd.DateOffset(weeks=1)
        elif date_range == 'all':
            start_date = stock_data['Last Trading Date'].min()  # Use the earliest date if no range specified

        stock_data = stock_data[stock_data['Last Trading Date'] >= start_date]

        # Plot filtered data
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data['Last Trading Date'], stock_data['Previous'], label='Closing Price')
        plt.plot(stock_data['Last Trading Date'], stock_data[f'{mv}-day SMA'], label=f'{mv}-day SMA', linestyle='--')

        # Add title, labels, and save the plot
        plt.title(f'Stock Closing Price and {mv}-day SMA - Last {date_range.capitalize()}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'./assets/time_series_{date_range}.png')
        print(f"Plot saved to './assets/time_series_{date_range}.png'")