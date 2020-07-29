#WAP to generate first n prime numbers

n=int(input("Please enter your number: "))
c=0
count=1
x=1
if n<=1:
  print("No Prime numbers available")
else:
 while True:
   count=1
   i=2
   x+=1
   while i<=x:
     if x%i==0:
       count+=1
     i+=1
   if count==2:
     print(x,end=' ')
     c+=1
   if c==n:
     break
print('',end='\n')                             
