import tkinter as tk
from tkinter import messagebox

# Parent class
class Zenith:
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def mutual_services(self):
        return [
            "Lines of credit",
            "Investment management and accounts",
            "Insurance"
        ]

    def unique_services(self):
        return []

# Retail Banking Division
class RetailBanking(Zenith):
    def unique_services(self):
        return [
            "Retirement and education accounts",
            "Loans and mortgages",
            "Checking and saving"
        ]

# Global Banking Division
class GlobalBanking(Zenith):
    def unique_services(self):
        return [
            "Multi-currency management services and products",
            "Foreign currency accounts",
            "Foreign currency credit cards",
            "Transborder advisory services",
            "Liquidity management"
        ]

# Commercial Banking Division
class CommercialBanking(Zenith):
    def unique_services(self):
        return [
            "Advisory services"
        ]

# GUI Application
def show_services():
    name = name_entry.get()
    division = division_var.get()

    if not name or division == "Select Division":
        messagebox.showerror("Input Error", "Please enter a name and select a division.")
        return

    if division == "Retail Banking":
        employee = RetailBanking(name)
    elif division == "Global Banking":
        employee = GlobalBanking(name)
    elif division == "Commercial Banking":
        employee = CommercialBanking(name)
    else:
        return

    services = f"Employee: {employee.employee_name}\n Division: {division}\n\n"
    services += "Mutual Services:\n" + "\n".join(employee.mutual_services()) + "\n\n"
    services += "Unique Services:\n" + "\n".join(employee.unique_services())

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, services)

# Main Window
root = tk.Tk()
root.title("Zenith Bank Employee Services")
root.geometry("550x550")
root.configure(bg="#ffffff")  # White background

# Zenith Bank colors
red_color = "#e30613"
gray_color = "#5e5e5e"

# Widgets with color styling
tk.Label(root, text="ZENITH BANK EMPLOYEE PORTAL", bg="#ffffff", fg=red_color, font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Employee Name:", bg="#ffffff", fg=gray_color, font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(root, width=40, font=("Arial", 11))
name_entry.pack(pady=5)

tk.Label(root, text="Select Division:", bg="#ffffff", fg=gray_color, font=("Arial", 12)).pack(pady=5)
division_var=tk.StringVar()
division_var.set("Select Division")
division_menu = tk.OptionMenu(root, division_var, "Retail Banking", "Global Banking", "Commercial Banking")
division_menu.config(bg=gray_color, fg="white", font=("Arial", 10))
division_menu.pack(pady=5)

tk.Button(root, text="Show Services", command=show_services, bg=red_color, fg="white", font=("Arial", 11, "bold")).pack(pady=10)

result_text = tk.Text(root, height=15, width=60, font=("Arial", 11), bg="#f0f0f0", fg=gray_color)
result_text.pack(pady=10)

root.mainloop()
