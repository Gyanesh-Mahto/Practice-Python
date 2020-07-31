city=input("Please enter your city: ")
if city=='Delhi':
  print("Hello Delhitte...Namaskar")
elif city=='Hyderabad':
  print("Hello Hyderabadi...Adab")
elif city=='Bangalore':
  print("Hello Kannadiga...Namaskara")
elif city=='Chennai':
  print("Hello Madrasi...Namaskara")
else:
  print("Hello...Namaskar")

# This program works fine until in input some space is entered before or after input.
# So, to remove spaces there are 3 methods:
# 1. lstrip()<--left strip method: It is used to remove spaces from left hand side or from beginning of string.(___xxx)
# 2. rstrip()<--right strip method: It is used to remove spaces from right hand side or end of string.(xxx___)
# 3. strip()<--strip method: It is used to remove spaces present in left hand side and right hand side(both side of string) of the
# string.(__xx__)

city=input("Please enter your city: ")
scity=city.strip()
if scity=='Delhi':
  print("Hello Delhitte...Namaskar")
elif scity=='Hyderabad':
  print("Hello Hyderabadi...Adab")
elif scity=='Bangalore':
  print("Hello Kannadiga...Namaskara")
elif scity=='Chennai':
  print("Hello Madrasi...Namaskara")
else:
  print("Hello...Namaskar")

# Another method of strip()
city=input("Please enter your city: ").strip()	#using method chaining
if city=='Delhi':
  print("Hello Delhitte...Namaskar")
elif city=='Hyderabad':
  print("Hello Hyderabadi...Adab")
elif city=='Bangalore':
  print("Hello Kannadiga...Namaskara")
elif city=='Chennai':
  print("Hello Madrasi...Namaskara")
else:
  print("Hello...Namaskar")
