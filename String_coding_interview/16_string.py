# Q16) Write the program for the following requirement:
# Input: ABAABBCA
#  Output: 4A3B1C

s=input("Please enter your string: ")
output=''
num=0
for x in s:
  if x not in output:
    num=s.count(x)
    output=output+str(num)+x
print(output)
