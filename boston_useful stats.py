import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('D:\Downloads\HousingData.csv')
print(data['CHAS'].value_counts())  
# sns.displot(data['RAD'],bins=24)# 24 bins for 24 range
# plt.show()
# useful things
# print(data.min())
# print(data.max())
# print(data.median())
# print(data.describe())#all in one