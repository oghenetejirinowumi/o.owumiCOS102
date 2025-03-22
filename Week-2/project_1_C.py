# Input names
name_1 = input("Enter the first name: ")
name_2 = input("Enter the second name: ")

# Input ages
age_1 = input("Enter the age of the first person: ")
age_2 = input("Enter the age of the second person: ")

# Swap the ages
age_1, age_2 = age_2, age_1  # Correct swapping

# Output the swapped values
print(f"{name_1} is now {age_1} years old.")
print(f"{name_2} is now {age_2} years old.")

