x = "english"
y = "math"

from abc import ABC, abstractmethod

class tutor(ABC):
 @abstractmethod
 def __init__(self, teacher):
     self.teacher = teacher
     




class tutorEnglish(tutor):
   def __init__(self, teacher, english, age):
     
      super().__init__(teacher)
      self.english = english
   def teach(self):
      print("I teach english")


class tutormath(tutor):
  def __init__(self, teacher, math, age):
    super().__init__(teacher)
    self.math = math

  def teach(self):
      print("i teach math")


student_choice = input("enter what you want tutoring on: ")

if student_choice == y:
  print(" Hello,  I am here to help you get better at math")
  S = tutormath("Bob","math", 40)
  print("Your teacher name is ", S.teacher)
if student_choice == x:
    print("Hi , I am here to help you to get better at english")
   
    S = tutorEnglish("maya","english", 36)
    print("Your teacher name is ", S.teacher)