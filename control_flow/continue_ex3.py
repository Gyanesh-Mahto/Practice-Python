cart=[10,20,3000,50,600,70]

for item in cart:
  if item>500:
    print("Order value is {} for which insurance is required. So, skipping this item".format(item))
    continue
  print("Processing Order: ",item)

'''
O/P:
----
Processing Order:  10
Processing Order:  20
Order value is 3000 for which insurance is required. So, skipping this item
Processing Order:  50
Order value is 600 for which insurance is required. So, skipping this item
Processing Order:  70
'''
