# Q9) Assume input string contains only alphabet symbols and digits. Write a program to sort characters of the string, first alphabet
# symbols followed by digits?

s=input("Please enter your string containing only alphabets and digits: ")
l=list(s)
output=''
output_alpha=''
output_num=''
for x in l:
  if x.isalpha():
    output_alpha=output_alpha+x
  if x.isdigit():
    output_num=output_num+x

output=''.join(sorted(output_alpha)+sorted(output_num))

print(output)

