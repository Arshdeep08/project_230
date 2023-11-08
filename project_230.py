import pandas as pd

dataset = pd.read_csv(r'country_vaccinations.csv')

print("shape of the given dataset: ", dataset.shape)

print("count of the column: ", len(dataset.columns))

print("name of parameters: ", dataset.columns)

print("Display empty row Data: ", dataset.loc[:, dataset.isna().any()])