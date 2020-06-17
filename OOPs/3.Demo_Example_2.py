#Demo Example with user defined values

class Student:
    def __init__(self, n, r, m):
        self.name=n
        self.rollno=r
        self.marks=m
    
    def print_method(self):
        print("Name: ", self.name)
        print("Roll No: ", self.rollno)
        print("Marks: ", self.marks)

s1=Student("Yuyutsu", 45, 95)
print("Print using reference variable which can access variables")
print("Name: ",s1.name)
print("Roll No: ",s1.rollno)
print("Marks: ",s1.marks)
print("\nPrint using reference variable which can access Methods")
s1.print_method()

s1=Student("John", 40, 76)
print("\nPrint using reference variable which can access variables")
print("Name: ",s1.name)
print("Roll No: ",s1.rollno)
print("Marks: ",s1.marks)
print("\nPrint using reference variable which can access Methods")
s1.print_method()

'''
O/P:
----
Print using reference variable which can access variables
Name:  Yuyutsu
Roll No:  45
Marks:  95

Print using reference variable which can access Methods
Name:  Yuyutsu
Roll No:  45
Marks:  95

Print using reference variable which can access variables
Name:  John
Roll No:  40
Marks:  76

Print using reference variable which can access Methods
Name:  John
Roll No:  40
Marks:  76
'''