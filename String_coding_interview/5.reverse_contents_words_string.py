# Q5) Write a Program To REVERSE internal content of each word?
s=input("Please enter your string: ")
l=s.split(' ')
s1=''
for x in l:
  x=x[::-1]
  s1+=x
  s1+=' '
print(s1)
