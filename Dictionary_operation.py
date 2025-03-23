#ALL BOUT DICTIONARY....
#*********************************************************************************************
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again"
}

#adding new items to dict...
programming_dictionary["Variables"] = "A place to store data"

#creating an empty dictionary...
empty_dictionary = {}

#wipe the exisitng dict...
#programming_dictionary = {}

#edit an item in the dict...
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary["Bug"])

for things in programming_dictionary:
  print(things)
  #for printing the values...abs
  print(programming_dictionary[things])

#*********************************************************************************************
  #e.g program to understand dictionaries n their working...
  student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  if student_scores[key] > 90 and student_scores[key] < 100:
    student_scores[key] = "Outstanding"
  elif student_scores[key] > 80:
    student_scores[key] = "Exceeds Expectations"
  elif student_scores[key] > 70:
    student_scores[key] = "Acceptable"
  else:
    student_scores[key] = "Fail"

student_grades = student_scores
# 🚨 Don't change the code below 👇
print(student_grades)

#***************88*****************************************************************************
#nesting tutorial...
#e.g. code:
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, list_of_cities):
  travel_log.append({"country": country, "visits" : visits, "cities" : list_of_cities})

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

#***********************************************************************************************
#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]