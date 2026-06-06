import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
data=pd.read_csv(r'D:\\Downloads\\HousingData.csv')
log_prices=np.log(data['MEDV'])
features=data.drop(['MEDV','INDUS','AGE'],axis=1)
model=LinearRegression().fit(features,log_prices)
pridicted_prices=model.predict(features)
mse=mean_squared_error(log_prices,pridicted_prices)
rmse=np.sqrt(mse)
features.mean()
log_prices
chas=2
rm=4
ptrratio=8
property_stats=features.mean().values.reshape(1,11)
property_stats_df = pd.DataFrame(property_stats, columns=features.columns)
value = model.predict(property_stats_df)
log_prices=np.log(data['MEDV'])
features=data.drop(['MEDV','INDUS','AGE'],axis=1)

property_stats=features.mean().values.reshape(1,11)
property_stats
model=LinearRegression()
model.fit(features,log_prices)
inflation_rate=27.51
def get_dollar_value(rm,ptrratio,chas=1,high_confidence=1):
    property_stats[0][4]=rm
    property_stats[0][8]=ptrratio
    property_stats[0][2]=chas
    value=model.predict(property_stats_df)
    
    if high_confidence:
        upper=value+2*rmse
        lower=value-2*rmse
        value=np.e**value*1000*inflation_rate
        upper=np.e**upper*1000*inflation_rate
        lower=np.e**lower*1000*inflation_rate
        return round(value,upper,lower)
    else:
        upper=value+rmse
        lower=value-rmse
        value=np.e**value*1000*inflation_rate
        upper=np.e**upper*1000*inflation_rate
        lower=np.e**lower*1000*inflation_rate
        return value,upper,lower

rm=int(input('enter number of rooms you want:'))
ptrratio=float(input('enter the students per teacher ratio:'))
chas=int(input('enter 1 for property next to river , 0 to away from river '))
high_confidence=int(input('enter 1 for high ranges , 0 for low ranges'))
value,upper,lower=get_dollar_value(rm,ptrratio,chas,high_confidence)
print(f'house price is:${round(value[0],2)}')
print(f'the value vary from ${round(lower[0],2)} to ${round(upper[0],2)}')
