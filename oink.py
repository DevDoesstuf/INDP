import csv

with open('INDP.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

def calculate_difficulty(passing_rate, difficulty):
    return (passing_rate * 0.5) + (difficulty * 0.5)

subjects = sorted(set(row['Subject'] for row in data if row['Subject']))

print("Subjects offered:")
for i, subject in enumerate(subjects, 1):
    print(str(i) + ". " + subject)

selection = input("Enter the number corresponding to the subject you want to view: ")

if selection.isdigit() and 1 <= int(selection) <= len(subjects):
    selected_subject = subjects[int(selection) - 1]
    
    classes = [row for row in data if row['Subject'] == selected_subject]
    for cls in classes:
        passing_rate = float(cls['Passing Rate'].strip('%'))
        difficulty = float(cls['Difficulty 1-100'])
        cls['Calculated Difficulty'] = calculate_difficulty(passing_rate, difficulty)
    sorted_classes = sorted(classes, key=lambda x: x['Calculated Difficulty'], reverse=True)
    
    print("\nClasses for " + selected_subject + " (sorted by easiest to hardest | these are calculated based of pass perctanges and self reported diffulty with 100 meaning easy and 1 difficult ):")
    for cls in sorted_classes:
        print(
            "Class: " + cls['Class'] +
            ", Subject: " + cls['Subject'] +
            ", Students Enrolled: " + cls['Number of Students Enrolled'] +
            ", Passing Rate: " + cls['Passing Rate'] +
            ", Number of 5's: " + cls["Number of 5's"] +
            ", Difficulty: " + cls['Difficulty 1-100'] +
            ", Calculated Difficulty: " + str(cls['Calculated Difficulty'])
        )
else:
    print("Invalid selection. Please run the script again and choose a valid subject number.")
