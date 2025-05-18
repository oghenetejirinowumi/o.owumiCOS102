import tkinter as tk
from tkinter import messagebox as msgbox

# RANDOM DATASET
employees = [
    {"name": "Mary Johnson", "department": "HR"},
    {"name": "John Doe", "department": "Logistics"},
    {"name": "Jane Smith", "department": "Finance"},
    {"name": "Peter Obi", "department": "Logistics"},
    {"name": "Adaeze Umeh", "department": "HR"},
    {"name": "Michael Lee", "department": "Finance"}
    {"name": "Chinwe Okoro", "department": "IT"}
    {"name": "Grace Isaac", "department": "IT"}
]

def welcomeMessage(name, dept, members):
    window=tk.Toplevel(root)
    window.title("Welcome")
    winow.geometry("400x250")

    tk.Label(window, text=f"Welcome {name} from {dept} Department.", font=("Arial",12,"bold")).pack(pady=10)
    tk.Label(window, text="Other members of your department:", font=("Arial",10)).pack(pady=5)

    for m in members:
        if m != name:
            tk.Label(window, text=f"- {m}").pack()


def verify_employee():
    name_input= name_entry.get().strip()
    dept_input=dept_entry.get().strip()

    found = False
    department_mambers = []

    for e in employees:
        if e["department"].lower() == dept_input.lower():
            department_members.append(e["name"])
        if e["name"].lower() == name_input.lower() and e["department"].lower() == dept_input.lower():
            found = True

    if found:
        welcomeMessage(name_input, dept_input, department_members)
    else:
        msgbox.showerror("Access Denied", "Employee not found in the specified department.")

def dept == dept_entry


# GUI
root = tk.Tk()
root.title("GIG LOGISTICS IDENTIFICATION SYSTEM")
root.geometry("500x300")

tk.Label(root, text="Welcome to GIG Logistics Verification System", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Enter your full name:").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

tk.Label(root, text="Enter your department:").pack()
dept_entry = tk.Entry(root, width=40)
dept_entry.pack(pady=5)

tk.Button(root, text="Verify", command=verify_employee).pack(pady=20)

root.mainloop()


import tkinter as tk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk

employees = [
    {"name": "Mary Evans", "Task": "Loading"},
    {"name": "Eyo Ishan", "Task": "Loading"},
    {"name": "DurojaiyeDare", "Task": "Transporting"},
    {"name": "AdamsAli", "Task": "Transporting"},
    {"name": "AndrewUgwu", "Task": "Reviewing Orders"},
    {"name": "StellaMankinde", "Task": "Reviewing Orders"},
    {"name": "JaneAkibo", "Task": "Customer Service"},
    {"name": "AgoJames", "Task": "Customer Service"},
    {"name": "MichellTaiwo", "Task": "Delivering Items"},
    {"name": "AbrahamJones", "Task": "Delivering Items"},
    {"name": "NicoleAnide", "Task": "Reviewing Orders"},
    {"name": "KosiKorso", "Task": "Reviewing Orders"},
    {"name": "AdeleMartins", "Task": "Transporting"},
    {"name": "EmmanuelOjo", "Task": "Transporting"},
    {"name": "AjayiFatima", "Task": "Customer Service"},
]

def date_today():
    from datetime import date
    return date.today()


def usernamevalidation(usernameinput_entry):
    username = usernameinput_entry.get()
    if username == "":
        msgbox.showerror("Error", "Please enter your full name.")
        return False
    if username.lower() == employees[0]["name"].lower():
        msgbox.showinfo("Welcome", f"Welcome {username} \n Your assigned task today {date_today()} is {employees[0]['Task']}")
        return True
    elif username.lower() != employees[0]["name"].lower():
        msgbox.showerror("Error", "You are not authorized to access this system.")
        return False
    
root=tk.Tk()
root.title("Employee BioLog System")
root.geometry("800x800")
root.configure(bg="lightblue")
root.resizable(False,False)

welcome_label=tk.Label(root,text="Welcome to Employee BioLog System",font=("Arial",20),fg="darkblue", bg="lightblue")
welcome_label.pack(pady=20)

usernameinput_label=tk.Label(root,text="Please enter your full name below:",font=("Arial",14),fg="black", bg="darkblue")
usernameinput_label.pack(pady=10)

usernameinput_entry=tk.Entry(root,width=50, height=10, text="Your Full Name")
usernameinput_entry.pack(pady=10)
usernameinput_entry.focus()

signin_button=tk.Button(root, text="Sign In", font=("Arial", 14), fg="white", bg="darkblue", command=lambda: usernamevalidation(usernameinput_entry))
signin_button.pack(pady=10)

root.mainloop()
# The code creates a simple GUI application using Tkinter for an Employee BioLog System.
     