# Q12) Write a program for the following requirement?
# 1) input: aaaabbbccz
# 2) output: 4a3b2c1z
s=input("Please input your string: ")
output=''
alpha=s[0]
count=1
for i in range(len(s)):
  if s[i]==alpha:
    count+=1
  else:
    output=output+str(count)+alpha
    alpha=s[i]
    count=1
  if i==len(s)-1:
    output=output+str(count)+alpha 
print(output)
