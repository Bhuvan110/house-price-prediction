import seaborn as sns
from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('D:\Downloads\HousingData.csv')
plt.figure(figsize=(16,12))  # bigger figure
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.show()