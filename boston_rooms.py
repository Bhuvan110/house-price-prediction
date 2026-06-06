import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('D:\Downloads\HousingData.csv')
sns.displot(data.RM)
plt.show()