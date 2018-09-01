class Lunch:
    def __init__(self, name):
        self.employee = Employee('Carl')
        self.customer = Customer(name)

    def order(self, foodname):
        self.customer.placeOrder(foodname, self.employee)

    def result(self):
        self.customer.printFood()   


class Customer:
    def __init__(self, name):
        self.foodname = None
        self.name = name
    def placeOrder(self, foodname, employee):
        self.foodname = employee.takeOrder(foodname)

    def printFood(self):
        print('ordered {0}'.format(self.foodname.name))


class Employee:
    def __init__(self, name):
        self.name = name 
    def takeOrder(self, foodname):
        return Food(foodname)


class Food:
    def __init__(self, name):
        self.name = name
        print("Take your {0}, please".format(self.name))
        
        
