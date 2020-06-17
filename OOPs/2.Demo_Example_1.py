#Demo Example with Hard coded values

class Student:              #Class
    '''Demo program'''      #doc string
    def __init__(self):     #Special Methods - Constructor
        self.name='Amit'    #Variables
        self.rollno=101     #Variables
        self.marks=90       #Variables

    def print_method(self): #Methods
        print("Name: ",self.name)
        print("Roll No: ",self.rollno)
        print("Marks: ",self.marks)

s=Student()
print("Print using reference variable which can access variables")
print("Name: ",s.name)
print("Roll No: ",s.rollno)
print("Marks: ",s.marks)
print("\nPrint using reference variable which can access Methods")
s.print_method()

'''
O/P:
Name:  Amit
Roll No:  101
Marks:  90

Print using reference variable which can access Methods
Name:  Amit
Roll No:  101
Marks:  90
'''