# Modular Programming

# def sayHello():
#     print("Hello!")
    
# sayHello()

# def sayHello(name="Jane"):
#     print("Hello, "+name+"!")
    
# sayHello("John")
# sayHello()

# Object Oriented Programming

# Data Abstraction -> hiding implementation details
# Encapsulation -> data and functions in a unit (class)
# Inheritance -> reusing existing code
# Polymorphism -> same functions behaving differently

class Student:
    def __init__(self, name, city, rollno):
        self.name = name
        self.city = city
        self.rollno = rollno
    
    def printData(self):
        print(self.name + " is from "+self.city)
        
john = Student('john', 'Bangalore', 18181)
print(john.city)

john.printData()

jane = Student('jane', 'Nagpur', 188181)
jane.printData()











