'''
Two operators we can use generally for string:

+-->'+' operator is used for concatination of strings

*-->'*' operator is used for repeatation of strings
'''
print("==============================================================")
print("Example-1: '+' operator")
print("Gyanesh"+"Mahto")	#GyaneshMahto
print('Gyanesh'+' '+'Mahto')	#Gyanesh Mahto

#While using '+' operator it is compulsary that both variables or arguments on which '+' operator is used must be string only otherwise we will get error.

#print('Gyanesh'+4)	#TypeError

print("==============================================================")
print("Example-2: '*' operator")
print('Gyanesh'*2)	#GyaneshGyanesh
print(3*'Gyanesh')	#GyaneshGyaneshGyanesh

#While using '*' operator it is compulsary that one argument must be integer only and other argument must be string. Order of argument is not important but one argument must be int only and other argument must be string.
#Float is not allowed
#print('Gyanesh'*3.0)	#Error


#Conclusion:
#string + string <---Valid
#string * string <---Invalid
#string * int <------Valid
#string + int<-------Invalid

#Membership operator
#-------------------
# in operator and not in operator is considered as membership operator
print("==============================================================")
print("Example - 3: Membership operator")
print('G' in 'Gyanesh')	#True
print('D' in 'Gyanesh')	#False
print('g' in 'Gyanesh')	#False

print('G' not in 'Gyanesh')	#False
print('D' not in 'Gyanesh')	#True
print('g' not in 'Gyanesh')	#True

print("==============================================================")
print("Example - 4: Membership operator")

main_string=input("Please enter main string: ")
sub_string=input("Please enter substring: ")

if sub_string in main_string:
    print("Substring is present in main string")
else:
    print("Substring is not present in main string")

#Comparison Operators:
#---------------------
#<, <=, >, >= are comparison operators for strings and ==,!= are equality operators
#Comparison will take place based on unicode comparison
#'Gyanesh' < 'Mahto'<------Comparison will take place based on unicode or ASCII comparison
#G unicode is 71 and M unicode is 77 so, above statement is true
print("==============================================================")
print("Example - 5: Comparison operator")
print('Gyanesh'<'Mahto')	#True
print(ord('G'))	#71
print(ord('M'))	#77
print('gyanesh'<'mahto')	#True
print(ord('g'))	#103
print(ord('m'))	#109

#If first character is same then comparison will take place with next character
print('Hello'<'Hi')	#True because 'H' in Hello and 'H' in Hi is same and comaprison takes place between 'e' in Hello and 'i' in Hi.
#ASCII of 'e' is 101 and 'i' is 105. So, 'i' is greater than 'e'. So, above statement is True

print("==============================================================")
print("Example - 6: ord")
s='Raja Harishchandra'
i=0
for ch in s:
  print("The character {} has ASCII or unicode {}".format(ch,ord(s[i])))
  i+=1
'''
O/P:
----
The character R has ASCII or unicode 82
The character a has ASCII or unicode 97
The character j has ASCII or unicode 106
The character a has ASCII or unicode 97
The character   has ASCII or unicode 32
The character H has ASCII or unicode 72
The character a has ASCII or unicode 97
The character r has ASCII or unicode 114
The character i has ASCII or unicode 105
The character s has ASCII or unicode 115
The character h has ASCII or unicode 104
The character c has ASCII or unicode 99
The character h has ASCII or unicode 104
The character a has ASCII or unicode 97
The character n has ASCII or unicode 110
The character d has ASCII or unicode 100
The character r has ASCII or unicode 114
The character a has ASCII or unicode 97
'''


print("==============================================================")
print("Example - 6: Comparison operator")

s1=input("Please enter first string: ")
s2=input("Please enter second string: ")
if s1==s2:
  print("first string and second string are equal")
elif s1<s2:
  print("first string is less than second string")
if s1>s2:
  print("first string is greater than second string")
