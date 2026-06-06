import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('D:\Downloads\HousingData.csv')
# print(data['RAD'].value_counts())  it is a rating from 1-24 (1: least access to highway . 24: easily access to highway)
sns.displot(data['RAD'],bins=24)# 24 bins for 24 range
plt.show()
