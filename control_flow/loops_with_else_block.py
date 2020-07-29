'''
Loops with else block:
----------------------
In python, special feature is available with else. it can be used with for loop as well as while loop and try except else finally also

if	for	while	try 
-	-	-
-	-	-	except
-	-	-
else	else	else	else
-	-	-
-	-	-	finally
-	-	-

If the loop is executed successfully without any break statement then only else block will be executed.
continue is not related to else statement. If break is used, then only else with loop is meaningful.
'''
cart=[10,20,30,40,50]

for item in cart:
  if item>500:
    print("We can't place this order since value is more than 500")
    break
  print("Processing item: ",item)
else:
  print("Congratulations all items processed successfully")

'''
O/P:
----
Processing item:  10
Processing item:  20
Processing item:  30
Processing item:  40
Processing item:  50
Congratulations all items processed successfully
'''
