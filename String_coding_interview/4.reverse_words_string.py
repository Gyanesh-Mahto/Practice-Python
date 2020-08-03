# Q4) Write a Program To REVERSE order of words present in the given string?
s=input("Please enter a string: ")
l=s.split(' ')
l1=l[::-1]
l1=' '.join(l1)  
print(l1)
