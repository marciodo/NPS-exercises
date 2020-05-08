course <- c(rep("superior", 2), rep("medio", 6), rep("fundamental", 2))
age <- c(34, 43, 31, 37, 24, 25, 27, 22, 21, 26)
salary <- c(1100.0, 1450.0, 960.0, 960.0, rep(600.0, 3), rep (450.0, 3))
jobYears <- c(5, 8, 6, 8, 3, 2, 5, 2, 3, 3)

df <- data.frame(course, age, salary, jobYears)

# Course variable
course_freq <- table(df$course)

# Get percentage values for each categorie
pct <- round(course_freq/sum(course_freq)*100)
# Place percentage value with the label names
lbls <- paste(rownames(course_freq), pct)
# Place a % symbol to the label text
lbls <- paste(lbls, "%", sep="")
pie(course_freq, labels=lbls, main="Course variable")