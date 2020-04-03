import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../../school_data.csv", sep=";", decimal=b',')
data.head()

# Exercise asks to use only the first 4 characteristics (column 0 is id)
first_four = data.iloc[:,1:5]
first_four.head()

# Grouping in histograms
turma_hist = first_four.loc[:, "Turma"].value_counts()
sexo_hist = first_four.loc[:, "Sexo"].value_counts()
# Idade (age) must be sorted in ascending order
idade_hist = first_four.loc[:, "Idade"].value_counts()
idade_hist = idade_hist.sort_index()
# For Altura (high) we will brake into 6 bins
altura_hist = pd.cut(data.loc[:,"Alt"], 6).value_counts()

print(turma_hist)
print(sexo_hist)
print(idade_hist)
print(altura_hist)

# Plot the histograms
#turma_hist.plot.bar()
#sexo_hist.plot.bar()
#idade_hist.plot.bar()
#data.loc[:,"Alt"].plot.hist(bins=7)
#plt.show()

fig, (altura_plot, sexo_plot) = plt.subplots(1, 2)
fig.suptitle('Vertically stacked subplots')
altura_plot = data.loc[:,"Alt"].plot.hist(bins=7)
sexo_plot = sexo_hist.plot.bar()
plt.show()