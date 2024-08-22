# -*- coding: utf-8 -*-
"""CIE2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1StblNWf62phGLDhP3MRWmufCaN9iqE00
"""

import pandas as pd
Data=pd.read_csv("/content/titanic.csv")
print (data)

data.describe()

data.head()

data.info()

data.isnull().sum()

Data.duplicated()

data.shape

Data.dtypes

data['Pclass'].unique()

import numpy as np
from scipy import stats
mean1=np.mean(data['Age'])
median1=np.median(data['Age'])
mode1=stats.mode(data['Age'],keepdims=True).mode[0]
mean2=np.mean(data['Fare'])
median2=np.median(data['Fare'])
mode2=stats.mode(data['Age'],keepdims=True).mode[0]
print("central tendency")
print("mean Age:", mean1)
print("median Age:", median1)
print("mode Age:", mode1)
print("mean Fare:", mean2)
print("median Fare:", median2)
print("mode Fare:", mode2)

import matplotlib.pyplot as plt
import pandas as pd
filtered_data = data[(data['Survived'].isin([0, 1])) & (data['Pclass'].isin([1, 2, 3]))]
counts = filtered_data.groupby(['Survived', 'Pclass'])['Survived'].count().unstack()
counts.plot(kind='bar', color=['red', 'pink','blue'])
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Total of Passengers')
plt.title('Num of Survived and Not Survived by plans')
plt.legend(title='Pclass')
plt.show()

import pandas as pd
data=pd.read_csv('/content/titanic.csv')
print(data)
null_values=data.isnull().sum()
titanic_filled_data=data.fillna(data.mean(numeric_only=True))
null_values,titanic_filled_data.head()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
mean=np.mean(data['Age'])
std=np.std(data['Age'])
print("mean:",mean)
print("std of data:",std)
threshold=3
outlier=[]
for i in data['Age']:
  z=(i-mean)/std
  if z>threshold:
    outlier.append(i)
print("outlier i the dataset is",outlier)
sns.boxplot(data['Age'])
plt.title("Boxplot")
plt.show()

