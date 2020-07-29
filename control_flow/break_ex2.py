cart=[10,20,30,50,600,70]

for item in cart:
  if item>500:
    print("For placing the order above 500, Insurance is required. So, can't place order")
    break
  print("Processing Order: ",item)
