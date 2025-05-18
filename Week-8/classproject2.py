import tkinter as tk
from tkinter import messagebox as msgbox


# Logic to calculate cost based on address and package mass
def calculate_cost(mass, address):
    address = address.strip().lower()
    try:
        mass = float(mass)
    except ValueError:
        msgbox.showerror("Input Error", "Package mass must be a number.")
        return None

    if address == "pau":
        return 2000 if mass >= 10 else 1500
    elif address == "epe":
        return 5000 if mass >= 10 else 4000
    else:
        msgbox.showerror("Location Error", "We currently only deliver to PAU or EPE.")
        return None


# Shows all delivery details and the cost
def delivery_details():
    customer_name = customername_entry.get()
    pickup_address = pickupaddress_entry.get()
    recipient_name = recipientname_entry.get()
    recipient_address = recipientaddress_entry.get()
    package_mass = packagemass_entry.get()

    cost = calculate_cost(package_mass, recipient_address)
    if cost is not None:
        msgbox.showinfo("Delivery Details", f"Customer Name: {customer_name}\n"
                            f"Pickup Address: {pickup_address}\n"
                            f"Recipient Name: {recipient_name}\n"
                            f"Recipient Address: {recipient_address}\n"
                            f"Package Mass: {package_mass} kg\n"
                            f"Delivery Cost: ₦{cost}")



# GUI Setup
root = tk.Tk()
root.title("WUMID LOGISTICS DELIVERY COST ESTIMATOR")
root.geometry("600x500")
root.configure(bg="lightblue")

tk.Label(root, text="Welcome To WUMID LOGISTICS", font=("Arial Black", 20), bg="lightblue", fg="darkblue").pack(pady=10)
tk.Label(root, text="Please enter the following details:", font=("Helvetica", 14), bg="lightblue").pack(pady=5)

# Entry Fields
def add_labeled_entry(label_text):
    tk.Label(root, text=label_text, font=("Helvetica", 14), bg="lightblue", fg="blue").pack(pady=2)
    entry = tk.Entry(root, width=35, font=("Helvetica", 14))
    entry.pack(pady=2)
    return entry

customername_entry = add_labeled_entry("Customer Name:")
pickupaddress_entry = add_labeled_entry("Pick-Up Address:")
recipientname_entry = add_labeled_entry("Recipient Name:")
recipientaddress_entry = add_labeled_entry("Recipient Address (PAU or EPE only):")
packagemass_entry = add_labeled_entry("Package Mass (kg):")

# Buttons
tk.Button(root, text="ESTIMATE COST", font=("Arial Black", 14), bg="darkblue", fg="white", command=delivery_details).pack(pady=10)
tk.Button(root, text="EXIT", font=("Arial Black", 14), bg="darkred", fg="white", command=root.quit).pack(pady=10)

root.mainloop()

