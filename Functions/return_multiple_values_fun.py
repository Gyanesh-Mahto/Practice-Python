def calc(n1, n2):
    Sum = n1+n2
    if n1>n2:
        Sub = n1-n2
    else:
        Sub = n2-n1
    Mul = n1*n2
    Div = n1/n2
    return Sum, Sub, Mul, Div

n1 = int(input("Please enter first number: "))
n2 = int(input("Please enter second number: "))
result = calc(n1, n2)
for i in result:
    print(i)

'''
I/P:
Please enter first number: 20
Please enter second number: 10

O/P:
30
10
200
2.0
'''