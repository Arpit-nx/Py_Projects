print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
Full_name = name1 + name2
lower_names = Full_name.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
Tens_place = t+r+u+e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
Unit_place = l+o+v+e
Final_score = Tens_place*10 + Unit_place
if Final_score < 10 or Final_score > 90:
  print(f"Your score is {Final_score}, you go together like coke and mentos.")
elif Final_score > 40 and Final_score < 50:
  print(f"Your score is {Final_score}, you are alright together.")
else:
  print(f"Your score is {Final_score}.")