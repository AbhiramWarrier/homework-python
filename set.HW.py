

age = int(input("enter your age: "))
adult_set ={18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}
teen_set = {12, 13, 14, 15, 16, 17}

if age in adult_set:
    print("you are allowed to drive a car")
    print("you are allowed to drink alcahol")
    print("you are allowed to vote")
elif age in teen_set:

    print("you are allowed to work a partime job")
else: 
    print("you are not allowed")
    

