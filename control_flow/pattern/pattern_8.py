#WAP to print inverted pyramid with * symbols

n=int(input("Please enter no. of rows: "))

for i in range(n):
  print(" "*i+"* "*(n-i))	#No of spaces every row: i and No. of * every row: n-i
