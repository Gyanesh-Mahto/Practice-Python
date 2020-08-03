# Q18) Write a program to find the number of occurrences of each
#  vowel present in the given string?

s=input("Please enter your string: ")
vowel='aeiouAEIOU'
output=''
for x in s:
  if x not in output:
    output=output+x
output=sorted(output)
for y in output:
  if y in vowel:
    print("character {} occurs {} times".format(y,s.count(y)))
