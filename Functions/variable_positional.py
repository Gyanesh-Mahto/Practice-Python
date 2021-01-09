def print_postional_variable(ps,*vr):
    print("Positional variable: {}".format(ps))
    for k in vr:
        print("Variable length arguments: {}".format(k))

print_postional_variable(10)
print("------------------------")
print_postional_variable(10,20,30)
print("------------------------")
print_postional_variable(10,"A",20,"B")
print("------------------------")

'''
O/P:
Positional variable: 10
------------------------
Positional variable: 10
Variable length arguments: 20
Variable length arguments: 30
------------------------
Positional variable: 10
Variable length arguments: A
Variable length arguments: 20
Variable length arguments: B
------------------------
'''