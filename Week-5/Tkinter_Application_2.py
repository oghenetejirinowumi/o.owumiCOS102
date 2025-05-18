import tkinter as tk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk

def welcomeMessage(username):
    window = tk.Toplevel(root)
    window.title("Adwin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is Python GUI with Tkinter")
    label_2.pack()

def submit():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Mary" and password == "cos102":
        welcomeMessage(username)
    else:
        msgbox.showerror("Login", "Invalid username or password. Please Try again")

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")

# Username
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="SUBMIT", command=submit)
submit_button.pack()

# Main loop
root.mainloop()

