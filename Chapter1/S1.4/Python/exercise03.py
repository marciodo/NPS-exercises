import pandas as pd
import matplotlib.pyplot as plt

number_used_transports = [2, 3, 2, 1, 2, 1, 2, 1, 2, 3, 1, 1, 1, 2, 2, 3, 1, \
                          1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 3]
                          
transport_freq = pd.Series(number_used_transports).value_counts()

print ("Frequency table:")
print (transport_freq)

plt.figure(num='Section 1.4 exercise 3')
plt.bar(['1', '2', '3'], transport_freq.array)
plt.title("Number of different transportation modes used daily")
plt.xlabel("Number of transportation modes")
plt.show()