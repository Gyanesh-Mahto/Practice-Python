'''
if-elif-else syntax:

if condition-1:
    Action-1
elif condition-2:
    Action-2
elif condition-3:
    Action-3
-
-
-
else:
    default action
'''

num=int(input("Please enter any number: "))
if num>0 and num%2==0:
    print("Even")
elif num>0 and num%2!=0:
    print("Odd")
else:
    print('Number is negative or zero')

