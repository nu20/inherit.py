class vehicle :
    def __init__(self,name,max_speed,mileage) :
     self.name = name
     self.max_speed = max_speed
     self.mileage = mileage
    def printinfo(self) :
     print(self.name)
     print(self.max_speed)
     print(self.mileage)

class bus(vehicle) :
  pass

obj = bus("thar" , 180 , 74)
obj.printinfo()