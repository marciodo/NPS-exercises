number_used_transports <- c(2, 3, 2, 1, 2, 1, 2, 1, 2, 3, 1, 1, 1, 2, 2, 3, 1,
                            1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 2, 3)
                            
transport_freq = table(number_used_transports)

print ("Frequency table:")
print (transport_freq)

barplot(transport_freq, main="Number of different transportation modes used daily", xlab="Number of transportation modes")