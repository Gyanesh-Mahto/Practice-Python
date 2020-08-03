# Q21) Write the program for the following requirement:
# 1) inputs:
# 2) s1='abcdefg'
# 3) s2='xyz'
# 4) s3='12345'
# 5) output: ax1, by2,cz3,d4,e5,f,g

s1=input("Please enter your first string: ")
s2=input("Please enter your second string: ")
s3=input("Please enter your third string: ")

i,j,k=0,0,0
output=''

while i<len(s1) or j<len(s2) or k<len(s3):
  if i<len(s1):
    output=output+s1[i]
    i+=1
  if j<len(s2):
    output=output+s2[j]
    j+=1
  if k<len(s3):
    output=output+s3[k]
    k+=1
print(output)
