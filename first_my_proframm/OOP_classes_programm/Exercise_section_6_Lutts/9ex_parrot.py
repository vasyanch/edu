class Scene:
    def __init__(self):
        self.cus = Customer()
        self.cle = Clerk()
        self.par = Parrot()
    def action(self):
        for i in (self.cus, self.cle, self.par):
            i.line()

class Super:
    def line(self): print(self.name + ':' + repr(self.says()))

class Customer(Super):
    name = "Customer"
    def says(self): return 'Guest'
    
    

class Clerk(Super):
    name = 'Clerk'
    def says(self): return "rab"

class Parrot(Super):
    name = 'Parrot'
    def says(self): return 'Popka durak'
    
    
