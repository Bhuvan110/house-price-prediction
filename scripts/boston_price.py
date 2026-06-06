# import seaborn as sns
from sklearn.linear_model import LinearRegression
from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('D:\Downloads\HousingData.csv')
# model=LinearRegression()
# model.fit(data['DIS'],data['NOX'])

plt.scatter(data['DIS'],data['NOX'])
plt.show()
