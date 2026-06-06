import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('D:\Downloads\HousingData.csv')
plt.hist(data.MEDV)
plt.xlabel('house price in 1000\'s')
plt.ylabel('number of houses')
plt.show()
