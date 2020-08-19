# Q14) Write a program to remove duplicate characters from the given
#  input String?
#  Input: AZZZBCDABBCDABBBBCCCCDDDDEEEEEF
#  Output: AZBCDEF

s=input("Please enter your string: ")
output=s[0]
for x in s:
      if x not in output:
        output=output+x
print(output)
  
