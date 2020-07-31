# How to access caharacters of string
#There are 2 methods:
#1. By using index
#2. By using slice operator

#1. By using index:
#We can access string element either by positive index(Left to Right: forward) or negative index(Right to Left: backward direction)
print("=================================================="*2)
print("Example 1: Access and print character with index")
name="Gyanesh"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])
#print(name[100])	#IndexError: string index out of range

print("===================================================="*2)
print("Example 2: display characters of given string index wise(both positive and negative)")
#WAP to display characters of given string index wise(both positive and negative)
s=input("Please enter any string: ")
i=0
for x in s:
  print("The character present at positive index {} and negative index {} is {}".format(i,i-len(s),s[i]))
  i+=1

#2. By using slice operator:
# When we want to access substring from a given string then we can use slice operator. By using index we can get a character but by
# using slice operator we can get a range of character or substring of character
# Syntax: s[begin:end:step]
# s[begin:end]: returns substring from begin index to end-1 index
#  begin is optional and default value is from beginning onwards that is 0
#  end is optional and default value is length of given string len(s)
# s[begin:end:step]
#  step means how much increments we want. Default value of step is 1 
print("===================================================="*2)
print("Example -3: Access substring from string through slice operator")
s='abcdefghijklmnopqrstuvwxyz'
print(s[2:7])	#cdefg
print(s[:7])	#abcdefg
print(s[2:])	#cdefghijklmnopqrstuvwxyz
print(s[:])	#abcdefghijklmnopqrstuvwxyz
print(s[2:7:1])	#cdefg: Every character is considered between index 2 to index 6
print(s[2:7])	#cdefg
print(s[2:7:2]) #ceg: Every second character is considered between index 2 to index 6
print(s[2:7:3]) #cf: Every third character is considered between index 2 to index 6
print(s[::1])	#abcdefghijklmnopqrstuvwxyz
print(s[::2])	#acegikmoqsuwy
print(s[::3])	#adgjmpsvy

# Slice operator rules:
#s[begin:end:step]
# All begin, end, step can be either positive or negative. So, step value can be positive or negative.
# If step is positive, we have to consider substring from left to right[Forward Direction] from begin to end-1
# If step is negative, we have to consider substring from right to left[backward Direction] from begin to end+1
# In slice operator, step value can't be zero
#print(s[::0]) #ValueError: slice step cannot be zero

#Either forward direction or backward direction, we can take both +ve and -ve values for begin and end index
#In forward direction:
# default value to begin: 0
# default value for end: len(s)

#In backward direction:
# default value to begin: -1
# default value for end: -(len(s)+1)

