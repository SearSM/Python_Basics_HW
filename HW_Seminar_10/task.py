# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)

# print(pd.get_dummies(data))

data['robot'], data['human'] = 0, 0     # Создание новых колонок со значением 0
data.loc[data['whoAmI'] == 'robot', 'robot'] = 1
data.loc[data['whoAmI'] == 'human', 'human'] = 1
data = data.drop(columns = ['whoAmI'])     # Удаление whoAmI колонки
print(data)