ages <- c(22, 22, 22, 22, 23, 23, 24, 24, 24, 24, 25, 25, 26, 26, 26, 26, 27, 28, 35, 40)

# Build table with the frequency, percentage, and cumulative percentage
age_freq = table(ages)
age_freq_norm = age_freq / length(ages)
age_freq_norm_cum = cumsum(age_freq_norm)

df = cbind(age_freq, age_freq_norm, age_freq_norm_cum)
colnames(df) <- c("Age Frequency", "Relative", "Relative Cumulative")

print("Age distribution frequency")
print(df)

# Exercise asks us to remove atipical ages: 35 and 40 in this case
ages_no_outlier = ages[ages < 30]
age_no_outlier_freq = table(ages_no_outlier)
age_no_outlier_freq_norm = age_no_outlier_freq / length(ages_no_outlier)
age_no_outlier_freq_norm_cum = cumsum(age_no_outlier_freq_norm)

df_no_outlier = cbind(age_no_outlier_freq, age_no_outlier_freq_norm, age_no_outlier_freq_norm_cum)
colnames(df_no_outlier) <- c("Age Frequency", "Relative", "Relative Cumulative")

print("")
print("Age distribution frequency without outliers")
print(df_no_outlier)
