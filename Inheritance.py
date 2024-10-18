class vehicle:
    def __init__(self, millage, name):
        self.millage = millage
        self.name = name
        
    def show(self):
        print(self.millage)
        print(self.name)
        print("any animal")

class bike(vehicle):
    def __init__(self, name , millage):
        super().__init__(name, millage)
        self.name = name
        self.millage = millage

    def display(self):
        print(self.name)
        print(self.millage)
       
    

v = vehicle("400cc","Benz")

b = bike("bmw","500cc")

b.display()
b.show()