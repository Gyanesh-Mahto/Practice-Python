class Test:
    def __init__(self):
        print("The Address of object pointed by self: ", id(self))
    
t=Test()
print("The Address of object pointed by t: ", id(t))

'''
O/P:
----
The Address of object pointed by self:  11590736
The Address of object pointed by t:  11590736
'''