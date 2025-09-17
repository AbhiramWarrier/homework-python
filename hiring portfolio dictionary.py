
my_dict = {}

my_dict["name"] = input("Enter your name: ")
my_dict["age"] = int(input("Enter your age: "))



if my_dict["age"] >= 18:
   
   user = input("enter your WE ")
   if user == "business and administration":
      print(my_dict["name"],", you are invited for a meeting")
   elif  user == "marketing and sales":
      print(my_dict["name"],", you are invited for a meeting")
   else: 
      print("your experience is not fit for the job")

else:
     print("you are too young to work a normal job")

    

