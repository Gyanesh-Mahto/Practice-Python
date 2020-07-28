'''
infinite loop: If in a loop, condition always satisfies then it will execute infinitely.
To stop we need some condition with break statement

while True:
   body
   if condition:
      break
'''

i=1
while True:
  print("Hello: ",i)
  i+=1
  if i==101:
    break
