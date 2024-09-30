import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data import Data

class Visual:
    def __init__(self, link) -> None:
        self.data = Data(link)
        pass


    def get_df(self):
        return self.data.df
    

    def time_series(self, mv=20):
        stock_data = self.get_df().copy()
        stock_data[f'{mv}-day SMA'] = stock_data['Previous'].rolling(window=mv).mean()

        plt.figure(figsize=(10, 6))
        plt.plot(stock_data['Last Trading Date'], stock_data['Previous'], label='Closing Price', color='blue', linestyle='-', linewidth=1)
        plt.plot(stock_data['Last Trading Date'], stock_data[f'{mv}-day SMA'], label=f'{mv}-day SMA', color='green', linestyle='--', linewidth=1)

        # Adding title and labels
        plt.title('Stock Closing Price and Moving Averages')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.xticks(rotation=45)

        # Save the plot as a PNG file
        file_path = './assests/time_series.png'
        plt.tight_layout()
        plt.savefig(file_path)

        plt.show()