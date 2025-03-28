from tabulate import tabulate

# Data representation
students = [
    ("Evelyn", 17, 5.5, 80, "Female"), ("Jessica", 16, 6.0, 85, "Female"), ("Somto", 17, 5.4, 70, "Female"),
    ("Edith", 18, 5.9, 60, "Female"), ("Liza", 16, 5.6, 76, "Female"), ("Madonna", 18, 5.5, 66, "Female"),
    ("Waje", 17, 6.1, 87, "Female"), ("Tola", 20, 6.0, 95, "Female"), ("Aisha", 19, 5.7, 50, "Female"), ("Latifa", 17, 5.5, 49, "Female"),
    ("Chinedu", 19, 5.7, 74, "Male"), ("Liam", 16, 5.9, 87, "Male"), ("Wale", 18, 5.8, 75, "Male"),
    ("Gbenga", 17, 6.1, 68, "Male"), ("Abiola", 20, 5.9, 66, "Male"), ("Kola", 19, 5.5, 78, "Male"),
    ("Kunle", 16, 6.1, 87, "Male"), ("George", 18, 5.4, 98, "Male"), ("Thomas", 17, 5.8, 54, "Male"), ("Wesley", 19, 5.7, 60, "Male")
]

# Display table
headers = ["Name", "Age", "Height", "Score", "Gender"]
print(tabulate(students, showindex=True, headers=headers, stralign="center", tablefmt="fancy_grid"))
