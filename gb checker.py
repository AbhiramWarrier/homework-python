rem = "remaining"
gb = int(input("enter how much GB you have: "))
used = int(input("enter how much you have used"))
remaining = gb - used
 
 
if remaining > 50:
  pass
  print("you hav enough left")
elif remaining <= 50 and remaining > 0:
 pass
 print("your amount of gb is almost over use it carefully")
elif remaining == 0:
 pass
 print("your amount of gb has been brought down to 0: ")
else: 
  pass
print("invalid input: used is more than total gb")
print("buy from your phone company")


    