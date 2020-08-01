# replace()
# It is used in replacing a string with another string.
# Sytax:
# s.replace(oldstring, newstring)
print("====================="*3)
print("Example - 1")
s='ABABABABABABA'
s1=s.replace('A', 'B')
print(s1)	#BBBBBBBBBBBBB

s='Gyanesh Mahto'
s1=s.replace(' ', '')
print(s1)	#GyaneshMahto

s='Hello World'
s=s.replace('Hello', 'Hi')
print(s)	#Hi World
print("Total No. of spaces: ", s.count(' '))	#Total No. of spaces:  1

# WAP to print no. of spaces in a string
s='Hello Bots Welcome to Earth'
print("Total No. of spaces: ", s.count(' '))	#Total No. of spaces:  4

# WAP to print no. of spaces in a string without count method
s='Hello Bots Welcome to Earth'
s1=s.replace(' ','')
print("Total No. of spaces: ", len(s)-len(s1))	#Total No. of spaces:  4

# replace() method is case sensitive
s='Hello world I am GBot'
s1=s.replace('hello', 'Hi')	
print(s1)	#Hello world I am GBot
# So, replace() is case sensitive.

# Q. string objects are immutable then how we can change content by using replace() method?
# Because in the existing object, changes will not happen. So, whatever changes we are doing, with that new object will be created
# and variable name is assigned to new object from old object and if no reference to old object is present then old object will be
# available for garbage collection.

s='Gyanesh Mahto'
print('String s: {} and address is {}'.format(s,id(s)))	#String s: Gyanesh Mahto and address is 139630903347568
s=s.replace(' ', '')
print('String s: {} and address is {}'.format(s,id(s)))	#String s: Gyanesh Mahto and address is 139630903347952
