# PYTHON CALCULATOR: SIMPLE INTEREST, COMPOUND INTEREST, ANNUITY PLAN

def simple_interest(P, R, T):
    return P * (1 + (R/100) * T)

def compound_interest(P, R, n, t):
    return P * (1 + R /(n * 100))**(n * t)

def annuity_plan(PMT, R, n, t):
    return PMT * (((1 + (R/n)^n*t) - 1)/ (R/n))

def main():
    print("Select a calculation:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Annuity Plan")

    choice = input("Enter your choice (1/2/3):")

    if choice == "1":
        P = float(input("Enter the principal amount(P):"))
        R = float(input("Enter the rate of interest (R in %):"))
        T = float(input("Enter the time (T in years):"))
        result = simple_interest(P,R,T)
        print(f"\n The total amount after {T} years will be: {result:.2f}")

    elif choice == "2":
        P = float(input("Enter the principal amount (P): "))
        R = float(input("Enter the annual interest rate (R in %): "))
        n = int(input("Enter the number of times interest will be compounded per year {n}: "))
        t = float(input("Enter the time (t in years): "))
        result = compound_interest(P, R, n, t)
        print(f"\nThe total amount after {t} years will be: {result:.2f}")

    elif choice == "3":
        PMT = float(input("Enter the annuity payment (PMT): "))
        R = float(input("Enter the annual interest rate (R in %): "))
        n = int(input("Enter the number of payments per year (n): "))
        t = float(input("Enter the time (t in years): "))
        result = annuity_plan(PMT, R, n, t)
        print(f"\nThe future value of the annuity after {t} years will be: {result:.2f}")

    else: print("Invalid Choice. Please select (1/2/3)")

