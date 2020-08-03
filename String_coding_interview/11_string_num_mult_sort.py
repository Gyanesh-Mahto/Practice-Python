# Q) Write a program for the following requirement?
# 1) input: a3z2b4
# 2) output: aaabbbbzz (sorted String)

s=input('Enter Some String where alphabet symbol should be followed by digit:')
l=list(s)
output=''
for x in l:
  if x.isalpha():
    alpha=x
  else:
    num=int(x)
    output=output+(alpha*num)
output=sorted(output)
output=''.join(output)
print("Input: ",s)
print("Output: ",output)

