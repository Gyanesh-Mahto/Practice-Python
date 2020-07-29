'''
pass statement: It is python specific terminology. It is a keyword in Python.
if we have defined a function and don't know the implementation of that function then we can just mention pass. If we are not mentioning anything then wrror can occur

So, wherever empty block is required. So, in such type of cases we have to replace empty block with pass statement. So, pass acts as placeholder for future implementation of empty block.

def f1():
  pass
'''
def f1():
  pass

'''
During definition of class, if we are not implementing then we can use pass
'''
class A:
  pass

class B:
  pass

class C:
  pass

x=100

if x>10:
  print("Success")
else:
  #pass
  print("Failure")

'''
Conclusions about pass:
-----------------------
1. pass statement acts as empty statement in python
2. It acts as place holder to implement future code
3. It can be used to define minimal classes and functions
4. To define abstract methods, pass statement is the best choice 
'''
