class Parent:
    def __init__(self, fname, lname) :
        self.firstname = fname
        self.lastname = lname

    def printFullName(self) :
        print(self.firstname, self.lastname)

class Child(Parent) :
    def __init__(self, fname, lname):
        Parent.__init__(self, fname, lname)

a1 = Child("Amirreza", "Soheili")
a1.printFullName()

a2 = Child("Ali", "Soheili")
a2.printFullName()