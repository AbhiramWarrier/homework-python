answer = "place"
try:
  

    place =str(input("enter where you want to go in the netherlands: "))
    if place.isalpha():
        print("this place does  exist")
        print("that is a good choice")
    else: 
        raise SyntaxError 
except SyntaxError: 
    print("the place is non alphabetic")
    


    


    





