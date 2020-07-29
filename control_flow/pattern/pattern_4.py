# WAP to print square pattern with alphabet symbols

n=int(input("Please enter number : "))

for i in range(n):
  print(str(chr(97+i)+' ')*n)
