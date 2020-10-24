from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
import pandas as pd

cancer_data = load_breast_cancer()

print(cancer_data.keys())
# print(cancer_data['DESCR'])

df = pd.DataFrame(cancer_data['data'], columns=cancer_data['feature_names'])

df['target'] = cancer_data['target']
# print(df.head())

#Building the logistic regressor model:
x = df[cancer_data.feature_names].values
y = df['target'].values

model = LogisticRegression(solver='liblinear')
model.fit(x, y)
print('Prediction for datapoint 0:', model.predict([x[0]]))
print(model.score(x,y))
