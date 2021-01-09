# Write a Function to find Factorial of given Number?

def factorial(n):
    fact = 1
    while n>1:
        fact = fact*n
        n=n-1
    return fact

n = int(input("Please enter the number for which you want factorial: "))
factorial_result = factorial(n)
print("The factorial of {} is = {}".format(n, factorial_result))

'''
O/P:
The factorial of 4 is = 24
'''
