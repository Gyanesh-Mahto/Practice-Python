# Q20) Write a program to check whether the given string is palindrome
# or not ?
# A string is said to be palindrome iff original string and its reversed strings are equal.

s1=input("Please enter your string: ")
s2=s1[::-1]
if s1==s2:
  print("Give string is palindrome")
else:
  print("Give string is not palindrome")

