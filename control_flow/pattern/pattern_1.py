#WAP to print given number of *s in a row

n=int(input("Please enter how many star to be printed: "))
i=0
for i in range(n):  
  print("*",end=' ')	#Here since by default end attribute will go to new line since default value of end is '\n'. So, we are
  i+=1			#changing that to end=' '
print('',end='\n')

