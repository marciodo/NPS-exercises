import pandas as pd

ages = [22, 22, 22, 22, 23, 23, 24, 24, 24, 24, 25, 25, 26, 26, 26, 26, 27, 28,\
        35, 40]
        
age_freq = pd.Series(ages).value_counts()
age_freq_norm = pd.Series(ages).value_counts(normalize=True)

# Build table with the frequency, percentage, and cumulative percentage
df = pd.DataFrame()
df["Age Frequency"] = age_freq
df["Relative"] = age_freq_norm
df = df.sort_index()
df["Relative Cumulative"] = df["Relative"].cumsum()

print("Age distribution frequency")
print(df)

# Exercise asks us to remove atipical ages: 35 and 40 in this case
ages_no_outlier = [x for x in ages if x < 30]
age_no_outlier_freq = pd.Series(ages_no_outlier).value_counts()
age_no_outlier_freq_norm = \
                 pd.Series(ages_no_outlier).value_counts(normalize=True)

df_no_outlier = pd.DataFrame()

df_no_outlier["Age Frequency"] = age_no_outlier_freq
df_no_outlier["Relative"] = age_no_outlier_freq_norm
df_no_outlier = df_no_outlier.sort_index()
df_no_outlier["Relative Cumulative"] = df_no_outlier["Relative"].cumsum()

print()
print("Age distribution frequency without outliers")
print(df_no_outlier)