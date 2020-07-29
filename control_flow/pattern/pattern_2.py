#WAP to print square pattern with * symbols

n=int(input("Please enter the square value: "))
for x in range(n):
  for y in range(n):
    print('*',end=' ')
  print('',end='\n')

print("========="*3)

for i in range(n):
  print('* '*n)

