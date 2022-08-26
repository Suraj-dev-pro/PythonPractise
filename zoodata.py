import pandas as pd

zoo_data = pd.read_csv("zoo_data-1.csv", encoding = 'utf-8',
							index_col = ["animal_name"])

# print first 5 rows of zoo data
print(zoo_data.head())
