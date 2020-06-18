class Student:
    def __init__(delf, n, r, m):
        delf.name=n
        delf.rollno=r
        delf.marks=m
    
    def print_method(delf):
        print("Name: ", delf.name)
        print("Roll No: ", delf.rollno)
        print("Marks: ", delf.marks)
    
s=Student("Gyan", 101, 90)
s.print_method()

'''
O/P:
Name:  Gyan
Roll No:  101
Marks:  90
'''