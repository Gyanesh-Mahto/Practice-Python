# Q3) Write a Program To REVERSE content of the given String by using while loop?

print("Method - 1")
s=input("Please enter a string: ")
i=len(s)-1
while i>=0:
  print(s[i],end='')
  i-=1
print(end='\n')

print("================================================================")
print("Method - 2")
s=input("Please enter a string: ")
output=''
i=len(s)-1
while i>=0:
  output+=s[i]
  i-=1
print(output)
