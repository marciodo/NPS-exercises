import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()
df["Course"] = 2*["superior"] + 6*["medio"] + 2*["fundamental"]
df["Age"] = [34, 43, 31, 37, 24, 25, 27, 22, 21, 26]
df["Salary"] = [1100.0, 1450.0, 960.0, 960.0] + 3*[600.0] + 3*[450.0]
df["Job Years"] = [5, 8, 6, 8, 3, 2, 5, 2, 3, 3]

# Course variable
course_freq = df.loc[:, "Course"].value_counts()
print("Histogram for course")
print(course_freq)

# Group Age variable
age_bins = pd.cut(df["Age"], (20, 25, 30, 35, 40, 45), \
                  labels=["(20, 25]", "(25, 30]", "(30, 35]", "(35, 40]", \
                          "(40, 45]"])
age_freq = age_bins.value_counts()
age_freq_norm = age_bins.value_counts(normalize=True)

age_df = pd.DataFrame()
age_df["Age frequency"] = age_freq
age_df["Relative"] = age_freq_norm
agd_df = age_df.sort_index()
print()
print("Histogram for age")
print(age_df)

# Group salary
salary_freq = df.Salary.value_counts()
salary_freq_norm = df.Salary.value_counts(normalize=True)
salary_df = pd.DataFrame()
salary_df["Salary frequency"] = salary_freq
salary_df["Relative"] = salary_freq_norm
salary_df = salary_df.sort_index()
print()
print("Histogram for salary")
print(salary_df)

# Analyze how salaries are different considering more than 3 years of job
print()
print("How salaries grow considering years of job")
print(df[["Salary", "Job Years"]].sort_values(by = "Job Years"))

# All plots on the same screen
fig, ((course_plt), (age_plt), (salary_plt)) = plt.subplots(1, 3)
fig.suptitle('Section 1.4 exercise 7')
fig.canvas.set_window_title('Section 1.4 exercise 7')

course_plt.set_title("Course variable")
course_plt.pie(course_freq, labels=course_freq.index, autopct='%1.1f%%')

age_plt.set_title("Age variable")
age_plt.bar(age_df.index.categories, age_df.values[:,0])

salary_plt.set_title("Salary variable")
# I didn't like the salary with the default distance between numbers, so I'm
# converting them to string to have one bar besides the other out of scale.
salary_plt.bar([str(sal) for sal in salary_df.index], salary_df.values[:,0])

plt.show()