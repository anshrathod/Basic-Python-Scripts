import pickle
import pandas as pd

b = {
    'Pclass': 1,
    'Age': 38,
    'SibSp': 1,
    'Parch': 0,
    'Fare': 71.25,
    'male': 0,
    'Q': 0,
    'S': 0,
}


class Titanic:
    def __init__(self):
        self.model = pickle.load(open("static/13-Logistic-Regression/titanicModel.sav", 'rb'))

    def predict(self, d):
        for key in d:
            d[key] = int(d[key])

        data = pd.DataFrame({
            'Pclass': [d['pclass']],
            'Age': [d['age']],
            'SibSp': [d['sibsp']],
            'Parch': [d['parch']],
            'Fare': [d['fare']],
            'male': [d['male']],
            'Q': [d['q']],
            'S': [d['s']],
        })
        return self.model.predict(data)


if __name__ == '__main__':
    a = {
            'pclass': 1,
            'age': '38',
            'sibsp': 1,
            'parch': '0',
            'fare': 75,
            'male': '0',
            'q': 0,
            's': 1,
        },
    t = Titanic()
    print(t.predict(a[0]))
