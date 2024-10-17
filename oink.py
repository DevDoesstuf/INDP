import pandas as pd

# Read the CSV file
df = pd.read_csv('INDP.csv')

# Display all unique subjects
unique_subjects = df['Subject'].unique()
print("Unique Subjects:")
for i, subject in enumerate(unique_subjects, 1):
    print(f"{i}. {subject}")

# Prompt user to select a subject
subject_choice = int(input("Choose a subject by number: "))
chosen_subject = unique_subjects[subject_choice - 1]

# Filter the DataFrame for the chosen subject
subject_df = df[df['Subject'] == chosen_subject]

# Calculate the ranking score
subject_df['Ranking Score'] = subject_df['pass rate'] * 0.5 + subject_df['difficulty'] * 0.5

# Sort by ranking score in descending order
sorted_subject_df = subject_df.sort_values(by='Ranking Score', ascending=False)

# Display the classes ranked by the calculated score
print(f"\nClasses in {chosen_subject} ranked by difficulty and pass rate:")
for index, row in sorted_subject_df.iterrows():
    print(f"Class: {row['class']}, Pass Rate: {row['pass rate']}, Difficulty: {row['difficulty']}, Ranking Score: {row['Ranking Score']:.2f}")
