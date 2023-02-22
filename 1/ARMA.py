# 使用时间序列模型预测数据

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# 读取数据
df = pd.read_csv('../data/source_data.csv', index_col=0)
df.head()

# 数据预处理
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df.head()

# 数据可视化
plt.figure(figsize=(12, 6))
plt.plot(df['value'])
plt.show()

# 数据分割
train = df[:'2018-12-31']
test = df['2019-01-01':]

# 模型训练
from statsmodels.tsa.arima_model import ARIMA
model = ARIMA(train, order=(1, 1, 1))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# 模型预测
pred = model_fit.forecast(steps=31)[0]

# 模型评估
from sklearn.metrics import mean_squared_error
from math import sqrt
rmse = sqrt(mean_squared_error(test, pred))
print('Test RMSE: %.3f' % rmse)

# 模型可视化
plt.figure(figsize=(12, 6))
plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(pred, label='Prediction')
plt.legend(loc='best')
plt.show()

# 模型保存
import pickle
pickle.dump(model_fit, open('model.pkl', 'wb'))

# 模型加载
model_fit = pickle.load(open('model.pkl', 'rb'))

# 模型预测
pred = model_fit.forecast(steps=31)[0]
pred

# 模型可视化
plt.figure(figsize=(12, 6))
plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(pred, label='Prediction')
plt.legend(loc='best')
plt.show()



