
user = int(input("what is your bank balance: "))
x = int(input("enter how many sales you have made today: "))

y = int(input("enter the cost of your product "))
z = int(input("enter the selling process"))
total_profit = (z - y) * x
print (" your profit is:", total_profit)
if total_profit < 0:
 print("exit")
 exit()
print(" your new balance is: ", total_profit + user)



