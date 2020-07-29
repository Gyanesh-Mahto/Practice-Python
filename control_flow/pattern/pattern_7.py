# WAP to print pyramid pattern with * symbols

n=int(input("Please enter no. of rows: "))
for i in range(n):
  print(' '*(n-i-1)+'* '*(i+1))
