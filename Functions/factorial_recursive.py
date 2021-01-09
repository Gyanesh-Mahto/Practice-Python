def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result

print("factorial of 0 is: ",factorial(0))
print("factorial of 4 is: ",factorial(4))
print("factorial of 5 is: ",factorial(5))

'''
O/P:
factorial of 0 is:  1
factorial of 4 is:  24
factorial of 5 is:  120
'''