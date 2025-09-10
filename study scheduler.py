
print("school starts at 9.00")
print("lessons at school")
subjects = list (("math", "english", "pause", "dutch", "gym"))

class_schedule ={
"math": "09:30  - 10:15 ",
"english":"10:15 - 11:00",
"pause" :  "11:00  - 11:30",
"dutch" :    "11:30  - 12:15",
"gym": "12:15 - 13:00",

}
for subject, schedule in class_schedule.items():
    print(f"{subject}: {schedule}")
    
print("class is over, you may leave the class")
