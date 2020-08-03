# Q10) Write a program for the following requirement?
# 1) input: a4b3c2
# 2) output: aaaabbbcc
s=input('Enter Some String where alphabet symbol should be followed by digit:')
l=list(s)
output=''
for x in l:
  if x.isalpha():
    alpha=x
  else:
    num=int(x)
    output=output+(alpha*num)
print("Input: ",s)
print("Output: ",output)
