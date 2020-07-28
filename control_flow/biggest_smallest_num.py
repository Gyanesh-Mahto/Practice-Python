#WAP to find biggest of 2 given numbers
num1=int(input('Please enter your first number: '))
num2=int(input('Please enter your second number: '))

if num1>num2:
    print('{} is greater'.format(num1))
elif num1<num2:
    print('{} is greater'.format(num2))
else:
    print('Both numbers are equal')
