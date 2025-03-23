#BASIC CALCULATOR...!!!
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

import os
import math

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 -n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return round(n1 / n2, 2)

def exponent(n1, n2):
  return n1 ** n2

def sq_root(n1):
  return math.sqrt(n1)

def root(n1, n2):
  return n1 ** (1/n2)
  
operators = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "^": exponent,
  "√": sq_root,
  "root": root
}
  
# def cal(n1, n2, op):
#   if op == '+':
#     return add(n1, n2)
#   elif op == '-':
#     return subtract(n1, n2)
#   elif op == '*':
#     return multiply(n1, n2)
#   elif op == '/':
#     return divide(n1, n2)
#   elif op == '^':
#     return exponent(n1, n2)
#   else:
#     return "Invalid operator"

# def calculator():
#     n1 = int(input("Enter the first number: "))
#     calculation_done = False
#     while not calculation_done:
#         for symbol in operators:
#             print(symbol)
#     op = input("Enter the operation to be performed: ")
#     n2 = int(input("Enter the next number: "))
#     result = cal(n1, n2, op)
#     print(f"{n1} {op} {n2} = {result}")
#     choice = input("Do you want to continue? Type 'y' for yes or 'n' for no: ")
#     if choice == 'n':
#         calculation_done = True
#     else:
#         n1 = result

#OPTIMIZED VERSION WITH THE USAGE OF DICTIONARY...!!!
def calculator():
  print(logo)

  n1 = float(input("Enter the first number: "))
  calculation_done = False
  while not calculation_done:
    for symbol in operators:
      print(symbol)
    n2 = float(input("Enter the next number: "))
    op = input("Enter the operation to be performed: ")
    for key in operators:
      if op == key:
        calculation_function = operators[op]#return add, subtract, multiply, divide, exponent
        answer = calculation_function(n1, n2)

        print(f"{n1} {op} {n2} = {answer}")
    else:
       print("Invalid operator")
       
    choice = input("""Do you want to continue? Type 'y' for yes, 'n' for no or 'r' for restart: """)
    if choice == 'n':
        calculation_done = True
    elif choice == 'y':
        n1 = answer
    else:
        clear()
        calculator()

calculator()
