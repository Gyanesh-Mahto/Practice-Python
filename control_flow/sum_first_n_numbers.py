n=int(input("Please enter any number: "))

i=0
Sum=0
while i<=n:
    Sum+=i
    i+=1

print("Total sum of numbers between 1 to {} is {}".format(n,Sum))
