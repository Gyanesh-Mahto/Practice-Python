# WAP to print right angle triangle pattern with * symbols

n=int(input("Please enter no. of rows: "))

for x in range(n):
  for y in range(x+1):
    print('* ',end=' ')
  print('',end='\n')
