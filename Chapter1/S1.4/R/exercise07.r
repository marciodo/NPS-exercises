course <- c(rep("superior", 2), rep("medio", 6), rep("fundamental", 2))
age <- c(34, 43, 31, 37, 24, 25, 27, 22, 21, 26)
salary <- c(1100.0, 1450.0, 960.0, 960.0, rep(600.0, 3), rep (450.0, 3))
jobYears <- c(5, 8, 6, 8, 3, 2, 5, 2, 3, 3)

df <- data.frame(course, age, salary, jobYears)

# Course variable
course_freq <- table(df$course)
print("Histogram for course")
print(course_freq)

# Get percentage values for each categorie
pct <- round(course_freq/sum(course_freq)*100)
# Place percentage value with the label names
lbls <- paste(rownames(course_freq), pct)
# Place a % symbol to the label text
lbls <- paste(lbls, "%", sep="")
pie(course_freq, labels=lbls, main="Course variable")

# Group Age variable
age_bins = pd.cut(df["Age"], (20, 25, 30, 35, 40, 45), \
                  labels=["(20, 25]", "(25, 30]", "(30, 35]", "(35, 40]", \
                          "(40, 45]"])
age_hist = hist(df$age)
age_freq = age_hist$counts
age_freq_norm = age_freq / length(df$age)

age_df <- data.frame(age_freq, age_freq_norm)
colnames(age_df) <- c("Age frequency", "Relative")
# Not working...
# Create strings for each histogram bin, showing the boundaries as in (20, 25]
for (idx in 2:length(age_hist$breaks))
    bin_bef <- age_hist$breaks[idx-1]
    bin_aft <- age_hist$breaks[idx]
    print(paste( "(", bin_bef, ", ", bin_aft, "]", sep=""))
    age_bins[idx - 1] <- paste( "(", bin_bef, ", ", bin_aft, "]", sep="")

rownames(age_df) <- age_hist$breaks
print()
print("Histogram for age")
print(age_df)