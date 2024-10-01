from visual import Visual

class Main:
    def __init__(self) -> None:
        self.visual = Visual("./dataset/bca.csv")


    def run(self):
        # self.visual.time_series(20)
        # self.visual.time_series(3, 'week')
        # self.visual.time_series(10, 'year')
        # self.visual.monthly_average()
        # self.visual.volume_analysis('all')
        self.visual.price_and_percent()
        pass


class Main2:
    def __init__(self) -> None:
        self.visual = Visual("./dataset/tkm.csv")


    def run(self):
        self.visual.time_series(100)
        self.visual.time_series(50, '5 year')
        self.visual.time_series(10, 'year')
        self.visual.time_series(5, 'month')
        self.visual.time_series(3, 'week')
        
        self.visual.monthly_average()

        self.visual.volume_analysis('all')
        self.visual.volume_analysis('5 year')
        self.visual.volume_analysis('year')
        self.visual.volume_analysis('month')
        self.visual.volume_analysis('week')

        self.visual.price_and_percent()
        self.visual.price_and_percent('5 year')
        self.visual.price_and_percent('year')
        self.visual.price_and_percent('month')
        self.visual.price_and_percent('week')
        pass

if __name__ == "__main__":
    Main2().run()



