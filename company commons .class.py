class S(object):
    
    def __init__(self, phone, company):
      self.phone = phone
      self.company = company
      
    def display(self):
       print(self.phone)
       print(self.company)
       

class Apple(S):
          
   def __init__(self, phone, company, OS, version):
         self.OS = OS
         self.version = version

         S.__init__(self, phone , company)

a = Apple('iphone 17', 'Apple', 'IOS', '18.6' )

a.display()
             
           
             


