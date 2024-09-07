import pandas as pd

data = {
    "Name": ["John", "Anna", "Peter"],
    "Age": [28, 24, 35],
    "City": ["New York", "Paris", "London"],
}


dataFrame = pd.DataFrame(data)
# print(dataFrame[dataFrame["Age"] > 25])


# read csv

dataset = pd.read_csv("Data.csv")

x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# print(x, y)


############################ numpy #################################################


import numpy as np


array = np.zeros(10)
# print(array.shape)

array = np.array([[1, 2, 3], [1, 2, 3]])

array = np.array([1,2,3,4,5,6])
print(array[array>3])
