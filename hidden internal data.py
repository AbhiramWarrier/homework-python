class Userdata:
     password = "opening"
     def __init__(self):
       
       self.__name = None
       self.__email = None
       self.__password = None

     def set_data(self, name , email, password):
      self.__name = name
      self.__email = email
      self.__password = password

      

     def show_name(self):
               print("user Name:",self.__name)
     def show_email(self):
                    print("user email", self.__email)
     def check_password(self, input_password):
          return input_password == self.__password
user = Userdata()
user.set_data("Alice", "alice@example.com", "mypassword")

user.show_name()
user.show_email()

while True:
    input_password = input("Enter password to check: ")
    if user.check_password(input_password):
        print("access granted")
        break
    else:
        print("access denied, try again")


                
