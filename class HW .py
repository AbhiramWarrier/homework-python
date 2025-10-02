class HabitsToKeep:
  
  def __init__(self,habit1, habit2):
   self.habit1 = habit1
   self.habit2 = habit2

good_habits = HabitsToKeep('reading', 'moving')

bad_habit = HabitsToKeep ('nail biting', 'negative selftalk')
bad_habit_list = [bad_habit.habit1, bad_habit.habit2]
good_habits_list = [good_habits.habit1,good_habits.habit2]
user_input = input("enter your good  habits")

good_habits_list.append(user_input)
print(good_habits.habit1)
user_input = input("enter your bad habit")
bad_habit_list.append(user_input)
print(bad_habit.habit1)


   