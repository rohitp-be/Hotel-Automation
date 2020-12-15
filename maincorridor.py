class MainCorridor:
    def __init__(self, cord= 0, floor=0, AC=True, Light=True, cost=15):
        self.AC = AC
        self.Light = Light
        self.cord = cord
        self.floor = floor
        self.cost = 15
        self.type = "main"

    def getStatus(self):
        self.AC = True
        self.Light = True
        return self

    def getCost(self):
        return self.cost