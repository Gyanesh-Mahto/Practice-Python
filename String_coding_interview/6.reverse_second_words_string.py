# Q6) Write a Program To REVERSE internal content of every second word present in the given string?
s=input("Please enter any string: ")
l=s.split(' ')
l1=''
i=0
for x in l:
  if i%2!=0:
    x=x[::-1]
    l1+=x
    l1+=' '
    i+=1
  else:
    l1+=x
    l1+=' '
    i+=1
print(l1)
