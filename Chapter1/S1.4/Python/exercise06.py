import pandas as pd
import matplotlib.pyplot as plt

num_kids = [3, 4, 3, 4, 5, 1, 6, 3, 4, 5, 3, 4, 3, 3, 4, 3, 5, 5, 5, 5, 6, \
            11, 10, 2, 1, 2, 3, 1, 5, 2]
                
# Build table with the frequency, percentage, and cumulative percentage
num_kids_freq = pd.Series(num_kids).value_counts()
num_kids_freq_norm = pd.Series(num_kids).value_counts(normalize=True)

df = pd.DataFrame()
df["Kids per Family Frequency"] = num_kids_freq
df["Relative"] = num_kids_freq_norm
df = df.sort_index()
df["Relative Cumulative"] = df["Relative"].cumsum()

print("Number of kids per family distribution frequency")
print(df)

plt.figure(num='Section 1.4 exercise 6')
plt.title("Distribution of number of kids per family")
plt.xticks(num_kids_freq.index)
plt.bar(num_kids_freq.index, num_kids_freq)
plt.show()