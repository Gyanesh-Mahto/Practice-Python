#WAP to generate prime numbers which are less than or equal the given number

n=int(input("Please enter your number: "))
count=1
if n<=1:
  print("No Prime numbers available")
else:
 for x in range(2,n+1):
   count=1
   i=2
   while i<=x:
     if x%i==0:
       count+=1
     i+=1
   if count==2:
     print(x,end=' ')
print('',end='\n')
