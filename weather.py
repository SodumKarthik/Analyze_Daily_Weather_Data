import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Weather.csv")
print(data.head())


print(data.describe())


print(data.info())


x=data["Rainfall"]
y=data["Evaporation"]
plt.plot(x,y)
plt.show()
