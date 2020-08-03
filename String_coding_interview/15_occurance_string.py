# Q15) Write a program to find the number of occurrences of each
#  character present in the given string?

s=input("Please enter your string: ")
output=''
for x in s:
  if x not in output:
    output=output+x
for ch in output:  
  print("character {} occurs {} times".format(ch,s.count(ch)))
