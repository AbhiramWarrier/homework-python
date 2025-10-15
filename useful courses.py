class Mathcourse:

    def skill(self):
        print("math is a useful skill")
        
    def solving(self):
        print("Math helps you solve problems")
    def job(self):
        print("math is needed for many jobs")

class Codingcourse:
    def skill(self):
        print("coding is a  useful skill")
    def solving(self):
        print("coding is a skill which teaches you how to solve problems")
    def job(self):
        print("coding is a skill which is required for a wide range of jobs")


obj_math = Mathcourse()
obj_code = Codingcourse()

for course in(obj_math,obj_code):

 course.skill()
 course.solving()
 course.job()