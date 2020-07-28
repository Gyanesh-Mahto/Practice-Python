#WAP to find biggest of 3 given numbers
num1=int(input('Please enter your first number: '))
num2=int(input('Please enter your second number: '))
num3=int(input('Please enter your third number: '))

if num1>num2 and num1>num3:
    print('{} is greater'.format(num1))
elif num2>num1 and num2>num3:
    print('{} is greater'.format(num2))
elif num3>num1 and num3>num2:
    print('{} is greater'.format(num3))
else:
    print('All numbers are equal')

