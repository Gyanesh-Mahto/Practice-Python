l=[10,20,0,5,0,30]
for i in l:
  if i==0:
    print("Can't divide 100 by 0")
    continue
  print("100/{}={}".format(i, 100/i))

'''
O/P:
----
100/10=10.0
100/20=5.0
Can't divide 100 by 0
100/5=20.0
Can't divide 100 by 0
100/30=3.3333333333333335
'''
