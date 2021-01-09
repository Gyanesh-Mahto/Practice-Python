
def Sum_Sub(n1, n2):
    Sum = n1+n2
    if n1>n2:
        Sub = n1-n2
    else:
        Sub = n2-n1
    return Sum, Sub

n1 = int(input("Please enter first number: "))
n2 = int(input("Please enter second number: "))
x,y = Sum_Sub(n1,n2)
print("Sum of given numbers {} & {} is = {}, Sub pf given numbers {} & {} is = {}".format(n1,n2,x,n1,n2,y))

'''
O/P:
Please enter first number: 30
Please enter second number: 20
Sum of given numbers 30 & 20 is = 50, Sub pf given numbers 30 & 20 is = 10
'''