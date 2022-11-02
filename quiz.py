from re import A
import pandas as pd
import numpy as np
import requests

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
df.apply(lambda x: x.max() - x.min())
print(df.apply(lambda x: x.max() - x.min()))

#Qn 2
df = pd.read_csv('quarters.csv')
print(df.head())


# [5 rows x 14 columns]

#qn 3

A

# qn 4

df = pd.DataFrame(np.random.randint(1,10,size=(10, 3)), columns=list('ABC'))
print(df)



# qn 5
albums = requests.get("https://jsonplaceholder.typicode.com/albums").json()

df = pd.DataFrame(albums)

print(df.head(101))

