import os
import pandas as pd # pandas 数据分析工具
import requests  # request 获取

path = r'/Github/python/machine_learning/ml_environment/iris/'

r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

with open(path + 'iris.data', 'w') as f:
    f.write(r.text)

os.chdir(path)

df = pd.read_csv(path + 'iris.data', names = ['sepal length', 'sepal width',
                                              'pental length', 'petal width',
                                              'class'])
df = df.head()
print(df['sepal length'])
