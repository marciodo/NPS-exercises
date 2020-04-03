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
#plt.show()import pandas as pd
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

fig, ((turma_plot, sexo_plot, idade_plot), \
      (altura_plot, boxplot_altura, reserved)) = plt.subplots(2, 3)
fig.suptitle('Section 1.3 exercises')
turma_plot.pie(turma_hist.array, labels=turma_hist.index, autopct='%1.1f%%')
turma_plot.set_title("Class ID variable")
sexo_plot.pie(sexo_hist.array, labels=sexo_hist.index, autopct='%1.1f%%')
sexo_plot.set_title("Gender variable")
idade_plot.bar(idade_hist.index, idade_hist.array)
idade_plot.set_title("Age variable")
idade_plot.set_ticks(idade_hist.index)
#altura_plot = data.loc[:,"Alt"].plot.hist(bins=7)

plt.show()