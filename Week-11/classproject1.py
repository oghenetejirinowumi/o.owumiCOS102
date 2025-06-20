import pandas as pd

# Load student data from CSV, drop any rows where Age is missing, and ensure Age is int
df = pd.read_csv("SIS.csv")
df = df.dropna(subset=["Age"])
df["Age"] = df["Age"].astype(int)

class Student:
    def __init__(self, mat_no, name, age, grade):
        self.mat_no = mat_no
        self.name = name
        self.age = age
        self.grade = grade

    def get_category(self):
        if 14 < self.age < 18:
            return "The_Pirates"
        elif 18 < self.age < 22:
            return "The_Yankees"
        elif 22 < self.age < 25:
            return "The_Bulls"
        elif self.age > 25:
            return self.get_error()
        else:
            return None  # Age ≤ 14 or exactly 14, 18, 22, 25

    def get_error(self):
        return "ERROR: Age above 25 is not allowed for classification."

# Lists for classified categories
pirates = []
yankees = []
bulls = []
errors = []

# Process and classify each student
for _, row in df.iterrows():
    student = Student(row["MatNo"], row["Name"], row["Age"], row["Grade"])
    category = student.get_category()

    if category == "The_Pirates":
        pirates.append(row)
    elif category == "The_Yankees":
        yankees.append(row)
    elif category == "The_Bulls":
        bulls.append(row)
    elif category is not None and "ERROR" in category:
        # Only attempt to log an error if category contains "ERROR"
        print(f"{student.name}: {category}")
        errors.append({
            "MatNo": student.mat_no,
            "Name": student.name,
            "Age": student.age,
            "Error": category
        })
    # If category is None and no “ERROR”, we simply skip (age out of all specified ranges)

def save_and_show(rows, filename):
    df_group = pd.DataFrame(rows)
    df_group.to_csv(f"{filename}.csv", index=False)
    print(f"\n{filename.replace('_', ' ').title()}:")
    print(df_group)

# Save and display each category if non-empty
if pirates:
    save_and_show(pirates, "The_Pirates")
else:
    print("\nThe Pirates: No students in this category.")

if yankees:
    save_and_show(yankees, "The_Yankees")
else:
    print("\nThe Yankees: No students in this category.")

if bulls:
    save_and_show(bulls, "The_Bulls")
else:
    print("\nThe Bulls: No students in this category.")

# If there were errors, save them to a separate CSV
if errors:
    df_errors = pd.DataFrame(errors)
    df_errors.to_csv("Classification_Errors.csv", index=False)
    print("\nClassification Errors:")
    print(df_errors)


                