# WAP to check whether the given number is prime or not?
n=int(input("Please enter your number: "))

if n<=1:
  print("Not Prime")
else:
  count=1
  i=2
  while i<=n:
    if n%i==0:
      count+=1
    i+=1
  if count==2:
    print("Prime")
  else:
    print("Not Prime")
    
