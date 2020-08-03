# Q8) Write a program to merge characters of 2 strings into a single string by taking characters alternatively?
s1=input("Please enter your first string: ")
s2=input("Please enter your second string: ")
output=''
i=0
j=0
while i<len(s1) or j<len(s2):
  if i<len(s1):
    output=output+s1[i]
    i=i+1
  if j<len(s2):
    output=output+s2[j]
    j=j+1

print(output)
