class ClassFooditem():
    i = "Fooditem"
    x = "healthy_list"
    def __init__(self):
        
        self.fooditem = ""
    def get_fooditem(self):
     self.fooditem = input("Enter what you daily eat?: ")

healthy_list = ['eggs', 'yoghurt', 'soup', 'fruits', 'bread', 'salad', 'rice' ]
fast_food_list = ['burger', 'pizza', 'fries']
dessert_list = ['ice cream ', 'cake', 'tiramisu']   

print("Your breakfast details.")

breakfast = ClassFooditem()
breakfast.get_fooditem()
if breakfast.fooditem in healthy_list:
        print("You are eating very healthy.")
else:
        print("You are eating unhealthy.")


print("Lunch details ")

lunch = ClassFooditem()
lunch.get_fooditem()
    
if lunch.fooditem in  healthy_list:
        print("You are eating healthy.")
else:
        print("You are eating unhealthy.")

print("Dinner details")
dinner = ClassFooditem()
dinner.get_fooditem()

if dinner.fooditem in  healthy_list:
        print("You are eating healthy.")
else:
        print("You are eating unhealthy.")

        print("You can have it for now but next time pick a healthier choice.")
        user = input("Enter what do you have for dessert? ")
        print("You can have it once in a while is not  a big deal")

