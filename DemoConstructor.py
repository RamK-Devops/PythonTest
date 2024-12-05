class calculator:

    k = 10 #class variable

    #default constructors
    def __init__(self, x, y):
        self.firstnumber = x
        self.secondnumber = y
        print("It's in the constructor")

    def addtwo(self):
        return self.firstnumber + self.secondnumber

    def multwo(self):
        return self.firstnumber * self.secondnumber * calculator.k

    def getData(self):
        print("It's in getData")


obj1 = calculator(10, 5)
obj1.getData()
print("sum:")
print(obj1.addtwo())
print("product:")
print(obj1.multwo())

