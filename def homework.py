def suggest_meal():

  goal =  str(input("please enter you goale.g., muscle,bulking "))
  if goal == "muscle":
       print("eat protein, lift weights")
       
       foods = ["chicken breast", "salmon", "eggs", "quin" "almonds"] 
       print("these foods  are packed with protein and that is exactly why help with building muscle")
       for i in range(4):
        print("-", foods[i])
  elif goal == "bulking":
       print("here is a list of foods that will help you to bulk up")

       print("chicken, salmon eggs")
    
       print("these are rich in protein and are sure to help you gain weight and muscle")
  else:

     print("i don`t have any suggestions for this goal")
suggest_meal()
    


           

        
           


       
       
        
       
 

