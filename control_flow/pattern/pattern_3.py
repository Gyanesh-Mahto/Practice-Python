# WAP to print square with provided fixed digit in every row

n=int(input("Please enter the number: "))
m=0
for x in range(n):
  m+=1
  for y in range(n):
    print('{}'.format(m),end=' ')
  print('',end='\n')

print("================="*3)

for i in range(n):
  print((str(i+1)+' ')*n)
