import math
import numpy as np  

def quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return print("No real roots")
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The roots of your quadratic equation are:", x1, "and", x2)

def cubic(valueA, valueB, valueC, valueD):
    coefficients = [valueA, valueB, valueC, valueD]
    roots = np.roots(coefficients)
    print("The roots of your cubic equation are:", roots)

def quartic(valueA, valueB, valueC, valueD, valueE):
    coefficients = [valueA, valueB, valueC, valueD, valueE]
    roots = np.roots(coefficients)
    print("The roots of your quartic equation are:", roots)

while True:
    print("\nWelcome to PolySolver - Your One and Only Polynomial Equation Solver")
    print("Please choose a polynomial equation to solve:")
    print("1. Quadratic")
    print("2. Cubic")
    print("3. Quartic")
    print("4. Exit")

    user_choice = input("Enter your choice (1 / 2 / 3 / 4): ")

    if user_choice == "1":
        a = int(input("Enter a value for A: "))
        b = int(input("Enter a value for B: "))
        c = int(input("Enter a value for C: "))
        quadratic(a, b, c)

    elif user_choice == "2":
        valueA = int(input("Enter a value for A: "))
        valueB = int(input("Enter a value for B: "))
        valueC = int(input("Enter a value for C: "))
        valueD = int(input("Enter a value for D: "))
        cubic(valueA, valueB, valueC, valueD)

    elif user_choice == "3":
        valueA = int(input("Enter a value for A: "))
        valueB = int(input("Enter a value for B: "))
        valueC = int(input("Enter a value for C: "))
        valueD = int(input("Enter a value for D: "))
        valueE = int(input("Enter a value for E: "))
        quartic(valueA, valueB, valueC, valueD, valueE)

    elif user_choice == "4":
        print("Exiting PolySolver. Goodbye!")
        break  # Exit the loop

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
