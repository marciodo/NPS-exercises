import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../school_data.csv", sep=";", decimal=b',')
df.head()

# Exercise asks to use only the first 4 characteristics (column 0 is id)
first_four = df.iloc[:,1:5]
first_four.head()

# Grouping in histograms
turma_hist = first_four.loc[:, "Turma"].value_counts()
sexo_hist = first_four.loc[:, "Sexo"].value_counts()
# Idade (age) must be sorted in ascending order
idade_hist = first_four.loc[:, "Idade"].value_counts()
idade_hist = idade_hist.sort_index()
# Exercise asks to group age below 18, between 18 and 21, and older than 21
idade_blocks = pd.cut(df.Idade, (0, 18,21, 100), labels=["<=18", "18-21", ">21"])
idade_blocks_hist = idade_blocks.value_counts()
# Use grouping above and group it by gender
idade_groups = df.groupby([idade_blocks, "Sexo"])
idade_por_sexo = idade_groups.size().unstack()
# For Altura (high) we will brake into 6 bins
altura_hist = pd.cut(df.loc[:,"Alt"], 6).value_counts()

print("Histogram for class ID")
print(turma_hist)
print("Histogram for gender")
print(sexo_hist)
print("Histogram for age")
print(idade_hist)
print("Histogram for age, in bins with <18, 18-21, and >21")
print(idade_blocks_hist)
print("Distribution of age per gender")
print(idade_por_sexo)
print("Histogram for height")
print(altura_hist)

# Plot the histograms
fig, ((turma_plot, idade_plot, altura_plot), \
      (sexo_plot, idade_por_sexo_plot, boxplot_altura)) = plt.subplots(2, 3)
fig.suptitle('Section 1.3 exercises')
fig.tight_layout(pad=3.0)
fig.canvas.set_window_title('Section 1.3 exercises')

turma_plot.set_title("Class ID variable")
turma_plot.pie(turma_hist.array, labels=turma_hist.index, autopct='%1.1f%%')

sexo_plot.set_title("Gender variable")
sexo_plot.pie(sexo_hist.array, labels=sexo_hist.index, autopct='%1.1f%%')

idade_plot.set_title("Age variable")
idade_plot.bar(idade_hist.index, idade_hist.array)

# Exercise asks to group age below 18, between 18 and 21, and older than 21 and
# then group by gender
idade_por_sexo_plot.set_title("Age Grouped by Gender")
idade_por_sexo_plot.bar(idade_por_sexo.index.categories, idade_por_sexo["M"], \
                        label="Men")
idade_por_sexo_plot.bar(idade_por_sexo.index.categories, idade_por_sexo["F"], \
                        bottom=idade_por_sexo["M"], label="Women")
# Placing values on the bar chart:
x_pos = 0
for index, row in idade_por_sexo.iterrows():
    idade_por_sexo_plot.text(x_pos, row["M"]/2, row["M"], ha='center', \
                             va='center')
    # For stacked bar, we have to add the Male position to Female, as the Female
    # bar is on the top of the Male bar.
    idade_por_sexo_plot.text(x_pos, row["M"]+row["F"]/2, row["F"], ha='center',\
                             va='center')
    idade_por_sexo_plot.text(x_pos, row["M"]+row["F"]+1, row["M"]+row["F"], \
                             ha='center')
    x_pos += 1
# More space to print the total amount
idade_por_sexo_plot.margins(y=0.1)
idade_por_sexo_plot.legend()

altura_plot.set_title("Height variable")
altura_plot.hist(df.loc[:,"Alt"], bins=7)
boxplot_altura.set_title("Boxplot for Height")
boxplot_altura.boxplot(df.loc[:,"Alt"])

plt.show()