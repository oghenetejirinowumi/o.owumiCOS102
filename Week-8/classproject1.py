import tkinter as tk
from tkinter import messagebox
import random
from datetime import date

class EmployeeSystem:
    def __init__(self):
        self.employees = [
            "Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu",
            "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones",
            "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"
        ]
        self.tasks = ["Loading", "Transporting", "Reviewing Orders", "Customer Service", "Delivering Items"]

    def check_employee(self, name):
        return name.title() in self.employees 

    def assign_task(self):
        return random.choice(self.tasks)

    def take_attendance(self, name):
        return f"{name}, your attendance for {date.today()} has been recorded."

    def refuse_access(self):
        return "You are not authorized to access the system."

# Create instance
system = EmployeeSystem()

# GUI
def sign_in():
    name = entry.get().strip().title()

    if system.check_employee(name):
        task = system.assign_task()
        message = system.take_attendance(name)
        messagebox.showinfo("Access Granted", f"{message}\nToday's task: {task}")
    else:
        messagebox.showerror("Access Denied", system.refuse_access())

# GUI setup
root = tk.Tk()
root.title("Employee BioLog System")
root.geometry("500x300")
root.configure(bg="lightblue")

tk.Label(root, text="Employee BioLog System", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=20)
tk.Label(root, text="Enter your full name:", font=("Arial", 12), bg="lightblue").pack()

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)
entry.focus()

tk.Button(root, text="Sign In", font=("Arial", 12), bg="darkblue", fg="white", command=sign_in).pack(pady=10)
tk.Button(root, text="Exit", font=("Arial", 12), bg="darkred", fg="white", command=root.quit).pack(pady=10)

root.mainloop()
