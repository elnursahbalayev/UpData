from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np


class linear_regression:

    def __init__(self):
        pass
    def train_test_bol(self, x, y, test_size=0.3):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=test_size, random_state=123)
        return self.x_train, self.x_test, self.y_train, self.y_test

    def modelleri_muqayise_et(self, x, y, test_size=0.3, alpha=1):
        models = [LinearRegression, Ridge, Lasso, ElasticNet]
        model_adlari = ['LinearRegression', 'Ridge', 'Lasso', 'ElasticNet']
        self.r2_scores = []
        self.train_test_bol(x, y, test_size=test_size)

        for model in models:
            if model == LinearRegression:
                m = model()
            else:
                m = model(alpha=alpha)
            m.fit(self.x_train, self.y_train)
            y_pred = m.predict(self.x_test)
            self.r2_scores.append(r2_score(self.y_test, y_pred))

        self.results_df = pd.DataFrame(np.array(self.r2_scores).reshape(1,-1), columns=model_adlari)
        print(f'En yaxsi model {model_adlari[np.array(self.r2_scores).argmax()]}:')
        return self.results_df