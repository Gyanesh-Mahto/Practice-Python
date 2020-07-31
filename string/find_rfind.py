# Find substrings
#----------------
# To find index of substring in main string there are 4 methods available:
# 1. find()
# 2. rfind()
# 3. index()
# 4. rindex()

# 1. find(): It always searches in given string from left to right (Begin to end). So, if matched substring is available in main string then it returns as follows:
# if substring exists then find() returns index of first occurance of substring in main string.
# else if substring does not exists then find() returns -1.

print("============"*5)
print("Example - 1")
s=('ABCBA')
print(s)	#ABCBA
print(s.find('B'))	#1
print(s.find('b'))	#-1

# 2. rfind(): It always searches in given string from right to left (end to begin). So, if matched substring is available in main string then it returs as follows:
# if substring exists then rfind() returns positive index of first occurance of substring in main string.

print("============"*5)
print("Example - 2")
s=('ABCBA')
print(s)	#ABCBA
print(s.find('B'))	#1
print(s.find('b'))	#-1
# else if substring does not exists then rfind() returns -1.

print("============"*5)
print("Example - 3")
s=('ABCBA')
print(s)	#ABCBA
print(s.rfind('B'))	#3
print(s.rfind('b'))	#

# If we want to search substring in given boundary index, then we can use find() methods as follows:
# find(substring, begin, end)
# substring is our given substring for searching
# This method will search from begin index to end-1 index

print("============"*5)
print("Example - 4")
s=('ABCDEFGHIJBA')
print(s)	#ABCBA
print(s.find('B', 3,8))	#-1
print(s.find('B', 1,8))	#1
print(s.rfind('F', 1,8))	#5
