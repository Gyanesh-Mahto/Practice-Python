a = 10
def f1():
    a = 777
    print(a)

def f2():
    print(a)

f1()
f2()

'''
O/P:
777
10
'''
#########################################################################33
a = 10
def f3():
    global a
    a = 777
    print(a)

def f4():
    print(a)

f3()
f4()

'''
O/P:
777
777
'''