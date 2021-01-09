def sum_variable(*n):
    total=0
    for k in n:
        total=total+k
    print("Total = {}".format(total))

sum_variable(10)
sum_variable(10,20)
sum_variable(10,20,30)
sum_variable(10,20,30,40)

'''
O/P:
Total = 10
Total = 30
Total = 60
Total = 100
'''