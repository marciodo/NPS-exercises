num_kids <- c(3, 4, 3, 4, 5, 1, 6, 3, 4, 5, 3, 4, 3, 3, 4, 3, 5, 5, 5, 5, 6, 11, 10, 2, 1, 2, 3, 1, 5, 2)

# Build table with the frequency, percentage, and cumulative percentage
num_kids_freq = table(num_kids)
num_kids_freq_norm = num_kids_freq / length(num_kids)
num_kids_freq_norm_cum = cumsum(num_kids_freq_norm)

df = cbind(num_kids_freq, num_kids_freq_norm, num_kids_freq_norm_cum)
colnames(df) <- c("Kids per Family Frequency", "Relative", "Relative Cumulative")

print("Number of kids per family distribution frequency")
print(df)

# The default barplot function suppress the x values when no totals are present.
# In this example there are no families with 7, 8, or 9 kids. I want these to be shown
# as empty spaces on the chart.

# Get the maximum and minimum number of kids per family, to build a range with them later
minX <- min(as.numeric(rownames(df)))
maxX <- max(as.numeric(rownames(df)))
# Build a new table using the minX and maxX as a range for the categories
num_kids_complete = table(factor(num_kids, levels=minX:maxX))

barplot(num_kids_complete, main="Distribution of number of kids per family")