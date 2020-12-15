from floor import Floor as flr
hotel = {}
movement = []
floors = 0
IPath= "input.txt"
floorObjects = {}

def readInput():
    count  = 0
    flag = True
    with open(IPath, 'r') as fInput:
        temp = {}
        for line in fInput:
            if count == 0:
                floors = int(line)                
            elif 2*floors >= count:
                if flag:
                    temp["MC"]=int(line)
                    flag = False
                else:
                    temp["SC"]=int(line)
                    flag = True
                if count/2 > 0 and count%2 == 0:
                    hotel[count/2] = temp
                    temp = {}
            count += 1

def getObjects(hotel):
    global floorObjects
    try:
        for fl in hotel:
            obj = flr(fl, hotel[fl])
        floorObjects =  obj.getObjects()
    except Exception as e:
        print e.message

def updateStatus(fobj):
    try: 
        for i in fobj:
            if i.type == "sub" and i.AC:
                light = i.Light
                ac = False
                i.setStatus(AC=ac, Light=light)
                break
    except Exception as e:
        print e.message

def getCost(fobj):
    fCost = 0
    try:
        for obj in fobj:
            fCost += obj.getCost()
    except Exception as e:
        print e.message
    finally:
        return fCost

def getMLimit(fobj):
    maxlimit = 0
    try:
        for obj in fobj:
            maxlimit = obj.getMaxLimit()
            break
    except Exception as e:
        print e.message
    finally:
        return maxlimit

def checkCost(floorObjects):
    for i in floorObjects:
        while getCost(floorObjects[i]) > getMLimit(floorObjects[i]):
            updateStatus(floorObjects[i])

def setStatus(flr, cord, flg):
    global floorObjects
    try:
        ob = floorObjects[int(flr)]
        for i in ob:
            if i.cord==cord and i.type=="sub":
                if flg:
                    i.setStatus(AC=i.AC, Light=True)
                else:
                    i.setStatus(AC=True, Light=False)
                checkCost(floorObjects)
    except Exception as e:
        print "no floor or corridor found ", e.message

def showStatus():
    global floorObjects
    print floorObjects
    for j in floorObjects:
        print "floor: ", j
        for objs in floorObjects[j]:
            print "Corridor: ", objs.type, objs.cord
            ac = "ON" if objs.AC else "OFF"
            light = "ON" if objs.Light else "OFF"
            print "AC: ", ac
            print "Light: ", light

readInput()
getObjects(hotel)
checkCost(floorObjects)

while 1 == 1:
    print("---------Menu----------")
    print("1. Movement")
    print("2. No Movement")
    print("3. Exit")
    choice = int(input())

    if choice == 1:
        floor = int(input("Enter floor number where movement happened : "))
        subCorridor = int(input("Enter sub corridor number where movement happened : "))
        setStatus(floor, subCorridor, True)
        showStatus()
    elif choice == 2:
        floor = int(input("Enter floor number where no movement happened : "))
        subCorridor = int(input("Enter sub corridor number where no movement happened : "))
        setStatus(floor, subCorridor, False)
        showStatus()
    else:
        break