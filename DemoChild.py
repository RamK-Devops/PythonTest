from DemoConstructor import calculator

class childmethod(calculator):
    z = 20

    #default constructors
    def __init__(self):
        calculator.__init__(self, 5, 10)


    def getCompleteData(self):
        print(self.z)
        print(self.k) # k is from Class Calculator
        print(self.addtwo()) # this is in class calculator
        return self.z + self.k + self.addtwo()

obj3 = childmethod()
Total =obj3.getCompleteData()
print("Total")
print(Total)
