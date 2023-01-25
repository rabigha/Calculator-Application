#Rabigh Ahmed

import cmath

def addition(a, b):
   return a + b

def subtraction(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

def expo(a, b):
   return a ** b

def quadratic(a, b, c):
   det = (b ** 2 - 4 * a * c)
   sol_1 = (-b + cmath.sqrt(det)) / (2 * a)
   sol_2 = (-b - cmath.sqrt(det)) / (2 * a)
   return sol_1, sol_2

operation = input(" Choose operation (Add, Subtract, Multiply, Divide, Power, Quadratic): ")

a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))

if operation == "Add":
   print("The sum is ", addition(a, b))

elif operation == "Subtract":
   print("The difference is ", subtraction(a, b))

elif operation == "Multiply":
   print("The product is ", multiply(a, b))

elif operation == "Divide":
   print("The quotient is ", divide(a, b))

elif operation == "Power":
   print("The answer is ", expo(a, b))

elif operation == "Quadratic":
   c = int(input("Enter a third number: "))
   print("The solutions are", quadratic(a, b, c))

else:
   print("This is invalid.")
