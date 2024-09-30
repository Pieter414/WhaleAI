import pandas as pd
import numpy as np

class Data:
    def __init__(self, link) -> None:
        self.df = pd.read_csv(link)
        self._clean_data()

    def _clean_data(self):
        # Perbaikan format tanggal
        self.df['Last Trading Date'] = self.df['Last Trading Date'].str.replace('Agt', 'Aug').str.replace('Mei', 'May')
        self.df['Last Trading Date'] = pd.to_datetime(self.df['Last Trading Date'], format='%d %b %Y')
        
        # Sort values dari tanggal
        self.df = self.df.sort_values(by='Last Trading Date')