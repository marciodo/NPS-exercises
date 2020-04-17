import pandas as pd
import matplotlib.pyplot as plt

healing_days = [15, 17, 16, 15, 17, 14, 17, 16, 16, 17, 15, 18, 14, 17, 15, 14,\
                15, 16, 17, 18, 18, 17, 15, 16, 14, 18, 18, 16, 15, 14]
                
# Build table with the frequency, percentage, and cumulative percentage
heal_days_freq = pd.Series(healing_days).value_counts()
heal_days_freq_norm = pd.Series(healing_days).value_counts(normalize=True)

df = pd.DataFrame()
df["Healing days Frequency"] = heal_days_freq
df["Relative"] = heal_days_freq_norm
df = df.sort_index()
df["Relative Cumulative"] = df["Relative"].cumsum()

print("Healing days distribution frequency")
print(df)

# Exercise asks to group less or equal healing days as "fast" and the others as
# "slow"
heal_days_blocks = pd.cut(healing_days, (0, 15, 100), labels=["fast", "slow"])
heal_days_blocks_freq = heal_days_blocks.value_counts()
#heal_days_blocks_freq_norm = \
#             pd.Series(heal_days_blocks).value_counts(normalize=True)

plt.figure(num='Section 1.4 exercise 5')
plt.title("Distribution of fast and slow healing times")
plt.pie(heal_days_blocks_freq, labels=heal_days_blocks_freq.index, \
	    autopct='%1.1f%%')
plt.show()