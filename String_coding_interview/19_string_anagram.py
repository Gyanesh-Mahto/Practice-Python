# Q19) Write a program to check whether the given two strings are
#  anagrams or not?
# Two strings are said to be anagrams iff both are having same content irrespective of
# characters position.
# Eg: lazy and zaly

s1=input("Please enter your first string: ")
s2=input("Please enter your second string: ")
s1=sorted(s1)
s2=sorted(s2)
if s1==s2:
  print("Both strings are anagram")
else:
  print("Both strings are not anagram")
