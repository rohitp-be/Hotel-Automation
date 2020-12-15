from subcorridor import SubCorridor as sc
from maincorridor import MainCorridor as mc
class Floor:
    floorList = []
    def __init__(self, floor=1, data = {}):
        self.floor = floor
        self.data = data
        self.maxlimit = 0
        self.setDStatus()

    def setDStatus(self):
        mData = self.data["MC"]
        sData = self.data["SC"]
        self.maxlimit = 15 * mData + 10 * sData
        for i in range(1, mData+1):
            self.floorList.append(mc(cord=i, floor=self.floor, mLimit=self.maxlimit))
        for j in range(1, sData+1):
            self.floorList.append(sc(cord=j, floor=self.floor, mLimit=self.maxlimit))
    
    def getObjects(self):
        t ={}
        for f in range(1, self.floor+1):
            t[f] = []
        try:
            for i in self.floorList:
                t[i.floor].append(i)
        except Exception as e:
            print e.message
        return t