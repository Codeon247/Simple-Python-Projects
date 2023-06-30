import matplotlib.pyplot as plt
from sklearn import datasets
iris = datasets.load_iris()
data = iris.data
plt.plot(data)

plt.xlabel("petal lenght in cm")

plt.ylabel("setal length in cm")

plt.title("Distribution Of the iris datasets ")

plt.grid()