from pymongo import MongoClient
client = MongoClient()
db = client.test

from sklearn.datasets import load_breast_cancer
import pandas as pd

cancer = load_breast_cancer()
data = pd.DataFrame(cancer.data, columns=[cancer.feature_names])

data.head()

import json
data_in_json = data.to_json(orient='split')
rows = json.loads(data_in_json)
db.cancer_data.insert(rows)

cursor = db['cancer_data'].find({})
df = pd.DataFrame(list(cursor))
print(df)
