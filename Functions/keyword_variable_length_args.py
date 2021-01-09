# key word variable length argument (kwargs)

def display(**n):
    for k,v in n.items():
        print(k,"=",v)

display(n1=10, n2=20)
display(rno=100,name="Durga",marks=70,subject="Java")

'''
n1 = 10
n2 = 20
rno = 100
name = Durga
marks = 70
'''