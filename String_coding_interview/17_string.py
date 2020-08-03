# Q17) Write the program for the following requirement:
#  Input: ABAABBCA
#  Output: A4B3C1

s=input("Please enter your string: ")
output=''
num=0
for x in s:
  if x not in output:
    num=s.count(x)
    output=output+x+str(num)
print(output)
