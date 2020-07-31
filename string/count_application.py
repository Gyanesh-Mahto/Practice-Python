# WAP to print index of all occurances of the given string
s=input("Please enter your string: ")
sub_s=input("Please enter substring to find: ")
i=s.find(sub_s)
if i==-1:
  print("Substring not available")
else:
  count=0
  while i!=-1:
    print("Substring {} is present at index {}".format(sub_s,i))
    i=s.find(sub_s,i+len(sub_s), len(s)) 
    count+=1
print("So, Total occurance of substring {} is {} times".format(sub_s,count))
