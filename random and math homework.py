import random
x = "user_choice"
user = int(input("enter a random number"))

factors = []

for i in range(1,user + 1):
 if user % i== 0:
    factors.append(i)
    random_factor = random.choice(factors)
    if user % 2 == 0:
     print("your number  has multiple factors")
else:
    print("your number  has only 2 factors")
    print("random factor of your number is: ", random_factor)
    
    