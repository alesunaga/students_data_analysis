# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Display the first few rows of data to get an overview
print("First few rows of the data:")
print(students.head())

# Summary statistics for all columns (including categorical data)
print("\nSummary statistics of the data:")
print(students.describe(include='all'))

# Calculate mean, median, mode, range, standard deviation, and MAD of math grades
math_grade_mean = students.math_grade.mean()
print(f"\nMean of math grades: {math_grade_mean:.2f}")

math_grade_median = students.math_grade.median()
print(f"Median of math grades: {math_grade_median:.2f}")

math_grade_mode = students.math_grade.mode()
print(f"Mode of math grades: {list(math_grade_mode)}")

# Range calculation: difference between max and min math grade
math_grade_range = students.math_grade.max() - students.math_grade.min()
print(f"Range of math grades: {math_grade_range}")

# Standard deviation calculation
math_grade_std = students.math_grade.std()
print(f"Standard deviation of math grades: {math_grade_std:.2f}")

# Median Absolute Deviation (MAD) calculation
math_grade_mad = students.math_grade.mad()
print(f"MAD (Median Absolute Deviation) of math grades: {math_grade_mad:.2f}")

# Visualization 1: Histogram of math grades
sns.histplot(x='math_grade', data=students)
plt.title("Histogram of Math Grades")
plt.xlabel("Math Grade")
plt.ylabel("Frequency")
plt.show()
plt.clf()

# Visualization 2: Box Plot of math grades
sns.boxplot(x='math_grade', data=students)
plt.title("Box Plot of Math Grades")
plt.xlabel("Math Grade")
plt.show()
plt.clf()

# Analyzing Mother's Job (Mjob) Column
# Calculate number of students with mothers in each job category
students_Mjob = students.Mjob.value_counts()
print("\nNumber of students with mothers in each job category:")
print(students_Mjob)

# Calculate proportion of students with mothers in each job category
students_Mjob_proportions = students.Mjob.value_counts(normalize=True)
print("\nProportion of students with mothers in each job category:")
print(students_Mjob_proportions)

# Visualization 3: Bar Chart of mother's job (Mjob)
sns.countplot(x='Mjob', data=students)
plt.title("Mother's Job Distribution (Count)")
plt.xlabel("Mother's Job")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
plt.clf()

# Visualization 4: Pie Chart of mother's job (Mjob)
students.Mjob.value_counts().plot.pie(autopct='%1.1f%%', figsize=(8, 8))
plt.title("Mother's Job Distribution (Proportion)")
plt.ylabel("")  # Hide the y-label for a cleaner pie chart
plt.show()
plt.clf()
