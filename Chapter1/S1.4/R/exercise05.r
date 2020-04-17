healing_days <- c(15, 17, 16, 15, 17, 14, 17, 16, 16, 17, 15, 18, 14, 17, 15, 14, 15, 16, 17, 18, 18, 17, 15, 16, 14, 18, 18, 16, 15, 14)

# Build table with the frequency, percentage, and cumulative percentage
heal_days_freq = table(healing_days)
heal_days_freq_norm = heal_days_freq / length(healing_days)
heal_days_freq_norm_cum = cumsum(heal_days_freq_norm)

df = cbind(heal_days_freq, heal_days_freq_norm, heal_days_freq_norm_cum)
colnames(df) <- c("Healing days Frequency", "Relative", "Relative Cumulative")

print("Healing days distribution frequency")
print(df)

# Exercise asks to group less or equal healing days as "fast" and the others as
# "slow"
heal_days_blocks = cut(healing_days, c(0, 15, 100), labels=c("fast", "slow"))
heal_days_blocks_freq = cbind(table(heal_days_blocks))

# Get percentage values for each categorie
pct <- round(heal_days_blocks_freq/sum(heal_days_blocks_freq)*100)
# Place percentage value with the label names
lbls <- paste(rownames(heal_days_blocks_freq), pct)
# Place a % symbol to the label text
lbls <- paste(lbls, "%", sep="")
pie(heal_days_blocks_freq, labels=lbls, main="Distribution of fast and slow healing times")