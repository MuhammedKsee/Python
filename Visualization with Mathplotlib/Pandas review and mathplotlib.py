# mathplotlib kutuphanesi
# gorsellestirme kutuphanesi
# line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd

df = pd.read_csv("iris.csv")

print(df.columns)

print(df.Species.unique())

print(df.info())

print(df.describe())

setosa = df[df.Species == "Iris-setosa"]
print(setosa.describe())

versicolor = df[df.Species == "Iris-versicolor"]
print(versicolor.describe())

## Gorsellestirme

import matplotlib.pyplot as plt

df1 = df.drop(["Id"],axis=1)
print(df1)

# df1.plot() #plot çizdirir
# plt.show() #çizilen plotu gösterir

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id,setosa.PetalLengthCm,color = "red",label = "setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color = "green",label = "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm,color = "blue",label = "virginica")


plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

df1.plot(grid = True,linestyle = ":",alpha = 0.5)
plt.show()

#Scatter plot

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color = "red",label = "setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color = "green",label = "versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color = "blue",label = "virginica")

plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWithCm")
plt.title("Scatter Plot")
plt.show()

#Histogram Plot

plt.hist(setosa.PetalLengthCm,bins = 10)
plt.xlabel("PetalLengthCm Values")
plt.ylabel("Frekans")
plt.title("Hist")
plt.show()

#Bar plot

import numpy as np

x = np.array([1,2,3,4,5,5,6,7])
y = x*2+5

plt.bar(x,y)
plt.title("Bar Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#subplot
df1.plot(grid=True,alpha = 0.9,subplots= True)
plt.show()

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color = "red",label = "Setosa")
plt.ylabel("Setosa-PetalLengthCm")
plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color = "green",label = "Versicolor")
plt.ylabel("Versicolor-PetalLengthCm")
plt.show()

