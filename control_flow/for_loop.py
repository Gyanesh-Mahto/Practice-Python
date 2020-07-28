'''
for loop syntax:
----------------
for x in sequence:
    Activity

Here x represent each element present in sequence.
Any sequence can be present: list, set, tuple, dict, string, range...
Activity will be performed as many number of elements present in sequence. So, time taken is equal to no. of elements present in sequence.
'''
s=input('Enter any string: ')
i=0
for x in s:
    print('The character present at {} index is: {}'.format(i, x))
    i+=1

'''
O/P:
The character present at 0 index is: G
The character present at 1 index is: y
The character present at 2 index is: a
The character present at 3 index is: n
The character present at 4 index is: e
The character present at 5 index is: s
The character present at 6 index is: h
The character present at 7 index is:  
The character present at 8 index is: M
The character present at 9 index is: a
The character present at 10 index is: h
The character present at 11 index is: t
The character present at 12 index is: o

'''
