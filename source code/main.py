from visual import Visual
import pandas as pd
import numpy as np

class Main:
    def __init__(self) -> None:
        self.visual = None
        pass

    def insert_data(self, link):
        self.visual = Visual(link)
        print(self.visual.time_series())
        return
    

if __name__ == "__main__":
    main = Main()
    main.insert_data("./dataset/bca.csv")



