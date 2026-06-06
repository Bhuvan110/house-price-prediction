import seaborn as sns
# from sklearn.linear_model import LinearRegression
# from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('D:\Downloads\HousingData.csv')
# sns.lmplot(x='TAX',y='RAD',data=data)
# plt.show()
# #just sns.lmplot demonstration
print(data['RM'].corr(data['MEDV']))
plt.scatter(data['RM'],data['MEDV'])
plt.show()

#this seaborn function plots graph b/w all possible columns(in data:14x14=166 graphs, heavy task) 
# sns.pairplot(data)
# plt.show()
