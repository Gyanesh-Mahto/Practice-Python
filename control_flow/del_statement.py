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
print(s2)
print(s3)
'''
All reference variables are deleted
'''
