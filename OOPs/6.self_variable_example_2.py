class Test:
    def __init__(self):
        print('Constructor')

    def value_x(self, x):
        print("Value of x: ", x)

t=Test()
t.value_x(10)

'''
O/P:
----
Constructor
Value of x:  10
'''