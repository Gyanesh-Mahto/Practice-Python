s=input("Please enter your string: ")

print("Method - 1")
print("Characters present in even index:")
i=0
while i!=len(s):
  if i%2==0:
    print(s[i])
  i+=1
i=0
print("Characters present in odd index:")
while i!=len(s):
  if i%2!=0:
    print(s[i])
  i+=1
print("==================================================")
print("Method - 2")
print("Characters at even index: ",s[0::2])
print("Characters at odd index: ",s[1::2])
