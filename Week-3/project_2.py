print("Welcome to Izfin Technology Annual Tax Revenue (ATR) Calculator")
print("This program calculates the Annual Tax Revenue (ATR) based on years of experience and age.")
staff_name = input("Enter your name: ")
experience = int(input("Enter your years of experience: "))
age = int(input("Enter your age: "))

if experience > 25 and age >= 55:
    print(f"Annual Tax Revenue ATR of {staff_name} is N5 600 000")

elif experience > 20 and age >= 45:
    print(f"Annual Tax Revenue ATR of {staff_name} is N4 800 000")

elif experience > 10 and age >= 35:
    print(f"Annual Tax Revenue ATR of {staff_name} is N1 500 000")

elif experience > 10 and age < 35:
    print(f"Annual Tax Revenue ATR of {staff_name} is N550 000")

else:
    print(f"Annual Tax Revenue ATR of {staff_name} is not available right now due to your age and experience")
