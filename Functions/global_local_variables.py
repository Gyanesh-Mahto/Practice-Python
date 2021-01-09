a = 10          #Global variable
def f1():
    b = 20      #local variable
    print(a)    #Global variable
    print(b)    #local variable

def f2():
    print(a)    #Global variable
#   print(b)    #Invalid

f1()
f2()

'''
O/P:
10
20
10
'''