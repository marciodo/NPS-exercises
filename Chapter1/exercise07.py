import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()
df["Course"] = 2*["superior"] + 6*["medio"] + 2*["fundamental"]
df["Age"] = [34, 43, 31, 37, 24, 25, 27, 22, 21, 26]
df["Salary"] = [1100.0, 1450.0, 960.0, 960.0] + 3*[600.0] + 3*[450.0]
df["Job Years"] = [5, 8, 6, 8, 3, 2, 5, 2, 3, 3]

# Plot Course variable
course_freq = df.loc[:, "Course"].value_counts()
plt.pie(course_freq, labels=course_freq.index, autopct='%1.1f%%')

# Group Age variable
age_bins = pd.cut(df["Age"], (20, 25, 30, 35, 40, 45), \
	              labels=["(20, 25]", "(25, 30]", "(30, 35]", "(35, 40]", \
	                      "(40, 45]"])
age_freq = age_bins.value_counts()
age_freq_norm = age_bins.value_counts(normalize=True)
# Not working...
age_df = pd.DataFrame(list(zip([age_freq.values, age_freq_norm.values])), index=age_bins.cat.categories, columns=["Age frequency", "Relative"])