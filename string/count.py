# count(): It is used to find the number of occurances of substring in given main string.
# Syntax:
# string.count(substring): It returns total count of occurance substring from main string.

print("Example - 1")
print("==========================="*3)
s='ABCBC'
print("Count of A: {}".format(s.count('A')))	#Count of A: 1
print("Count of B: {}".format(s.count('B')))	#Count of B: 2
print("Count of C: {}".format(s.count('C')))	#Count of C: 2
print("Count of F: {}".format(s.count('F')))	#Count of F: 0
print("Count of 'BC': {}".format(s.count('BC')))	#Count of 'BC': 2
print("Count of 'BCB': {}".format(s.count('BCB')))	#Count of 'BCB': 1

# We can also count substring in given boundary values. It is represented as follows:
# string.count(substring,begin,end)
# Retuns the number of occurance of substring from begin index to end-1 index
print("Example - 2")
print("==========================="*3)
s='Gyaneshyan'
print("count of 'yan': {}".format(s.count('yan', 1,10)))	#count of 'yan': 2
print("count of 'yan': {}".format(s.count('yan', 1,8)))	        #count of 'yan': 1
print("count of 'yan': {}".format(s.count('yan', 1,800)))	        #count of 'yan': 1

s='BBBBB'
print("Count of 'BB': {}".format(s.count('BB',1,800)))	#Count of 'BB': 2
print("Count of 'BBB': {}".format(s.count('BBB',1,800)))	#Count of 'BB': 1

