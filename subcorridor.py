class SubCorridor:
    light_cost = 5
    ac_cost = 10
    def __init__(self, cord=0,  floor=0, AC=True, Light=False):
        self.AC = AC
        self.Light = Light
        self.cost = 10
        self.cord = cord
        self.floor = floor
        self.type = "sub"
    
    def setStatus(self, AC=True, Light=False):
        self.AC = AC
        self.Light = Light
        self.cost = self.getCost() 

    def getStatus(self):
        return self

    def getCost(self):
        a_cost = self.ac_cost if self.AC else 0
        l_cost = self.light_cost if self.Light else 0
        self.cost = a_cost + l_cost
        return self.cost