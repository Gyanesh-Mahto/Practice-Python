# Q13) Write a program for the following requirement?
#  Input: a4k3b2
#  Output: aeknbd
# In this example the following two functions are required to use
# 1) ord(): To find unicode value for the given character
#  Eg: print(ord('a')) #97
# 2) chr(): To find corresponding character for the given unicode value
#  Eg: print(chr(97)) # a

s=input("Please enter your string: ")
output=''
alpha=''
for i in range(len(s)):
  if i%2==0:
    num=ord(s[i])
    output=output+s[i]
  elif i%2!=0:
    num1=int(s[i])
    num=num+num1
    alpha=chr(num)
    output=output+alpha
print("output: ",output)
