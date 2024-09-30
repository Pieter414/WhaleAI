from visual import Visual

class Main:
    def __init__(self) -> None:
        self.visual = Visual("./dataset/bca.csv")

    def run(self):
        # self.visual.time_series(20)
        # self.visual.time_series(3, 'week')
        # self.visual.time_series(10, 'year')
        self.visual.monthly_average()


if __name__ == "__main__":
    Main().run()



