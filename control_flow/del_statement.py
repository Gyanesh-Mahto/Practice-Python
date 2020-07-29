'''
del statement:
--------------
del is a keyword in Python. del means delete. It is used to delete a variable automatically so that corresponding object will be eligible for garbage collection
.
Example:
x=10

Now after some time we want to delete this reference variable x pointing to object 10. We can do that by using:

del x

After deleting this variable we can't use that object again.
'''
'''
print("=================="*3)
print("Example-1")
x=10
print(x)
del x
x+=1
print(x)
'''
'''
O/P:
----
10
Traceback (most recent call last):
  File "del_statement.py", line 18, in <module>
    x+=1
NameError: name 'x' is not defined
'''

'''
del statement is used to improve free memory
'''
print("====================="*3)
print("Example-2")
s1='Gyanesh'
s2=s1
s3=s2
del s1
#print(s1)
print(s2)
print(s3)
'''
Example-2
Gyanesh
Gyanesh
'''
'''
This proves that del statement only deletes reference variable corresponding to the object and not object itself.
'''
print("====================="*3)
print("Example-3")
s1='Gyanesh'
s2=s1
s3=s2
del s1,s2,s3
#print(s1)
#print(s2)
#print(s3)
'''
All reference variables are deleted and object is now available for garbage collection. So, once all reference variables pointing to object is deleted then only object will be available for garbage collection.
'''
'''
del vs immutable objects:
-------------------------
immutable objects are the objects on which we can't perform any changes
'''
s="durga" #We can delete reference variable s by using: del s
#del s #Valid	
#del s[0] #But we can't delete the elements present in immutable object like del s[0]<--Invalid

'''
del vs None:
------------
By using del, reference variable will be deleted and object will be by default available for garbage collection if there is no other reference variable pointing to that object.

x=10
del x
print(x)  #NameError: After deleting variable we can't access that variable

But when we use None, then for example x=10, x is pointing to object 10. But when we do x=None, then x points to None object instead of 10. So, 10 will be available for garbage collection and x points to None.

x=10
x=None
print(x)  #None
'''
print("=========================="*3)
print("Example -4")
x=10
x=None
print(x)  #None
'''
Advantage: The chance of failing python program with memory problems will be very less so that python application will become more robust.
'''
