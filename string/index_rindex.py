# index() method is also used to find substring from main string from left to right(begin to end).
# It returs as follows:
# If substring is found then index() method returns index of first occurance of substring
# But if substring is not found in main string then index() will generate ValueError instead of -1 as compared to find().

print("============="*5)
print("Example - 1")
s='ABCBA'
print(s)
print(s.index('B'))	#1
#print(s.index('F'))	#ValueError

# rindex() method is also used to find substring from main string from right to left(end to begin).
# It returs as follows:
# If substring is found then index() method returns index of first occurance of substring from right to left.
# But if substring is not found in main string then index() will generate ValueError instead of -1 as compared to find().

print("============="*5)
print("Example - 2")
s='ABCBA'
print(s)
print(s.rindex('B'))	#3
#print(s.rindex('F'))	#ValueError


print("============="*5)
print("Example - 3: Mail ID example")
mail=input("Please enter valid mail id: ")
try:
  i=mail.index('@')
  print("You have entered valid mail id.")
except ValueError:
  print("You have entered invalid mail id. Please use '@' for mail id")

# If we want to search substring in given boundary index, then we can use index() methods as follows:
# index(substring, begin, end)
# substring is our given substring for searching
# This method will search from begin index to end-1 index

print("============="*5)
print("Example - 4")
s='ABCDEFGHIJBM'
print(s)
#print(s.index('B',3,8))	#ValueError
print(s.index('B',1,8))		#1
print(s.rindex('B',3,11))	#10
#print(s.rindex('B',3,8))	#ValueError
print(s.index('BCD',1,8))		#1
print(s.index('BCD',1,1000))		#1

