import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
 
df=pd.read_csv('p1_diamonds.csv')
 
#print(df.head(10).to_string())

#Удаление unnamed столбца axis = 1 означает что мы удаляем столбец

df = df.drop(['Unnamed: 0'], axis =1)

#Создание переменных для категорий

categorical_features = ['cut', 'color', 'clarity']
le = LabelEncoder()

#Замена категорий н численные значения
for i in range(3):
	new = le.fit_transform(df[categorical_features[i]])
	df[categorical_features[i]] = new

#print(df.head(10).to_string())

X = df[['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']]
y= df[['price']]

#разделение данных на тренировочный и тестовы наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 25, random_state= 101) 

#тркнировка 
regr = RandomForestRegressor(n_estimators = 10, max_depth = 10, random_state = 101)
regr.fit(X_train, y_train.values.ravel())

#прогнозирование 
predictions = regr.predict(X_test)

result = X_test
result ['price'] = y_test
result['prediction'] = predictions.tolist()
print(result.to_string())

#определение оси х
x_axis = X_test.carat

#построение графиков 

plt.scatter(x_axis, y_test, c= 'b', alpha = 0.5, marker = '.' , label = 'Real')
plt.scatter(x_axis, predictions, c= 'r', alpha = 0.5, marker = '.' , label = 'predicted')
plt.xlabel('Carat') 
plt.ylabel('Price')
plt.grid(color = '#D3D3D3', linestyle = 'solid')
plt.legend(loc = 'lower right')
plt.show()
