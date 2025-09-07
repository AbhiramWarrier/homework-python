from datetime import datetime
from datetime import date
exam_date = datetime(2025, 10, 30)
today= datetime.today()

difference = exam_date - today
print("The exam is on 30 october")
print(f"You have {difference.days} days and {difference.seconds} seconds")

print("Please study hard, good luck")
print ("Whoever passes the exam gets to go to college")

print ("Maths", "English", "Dutch")

print("Your results will come after 4 weeks")