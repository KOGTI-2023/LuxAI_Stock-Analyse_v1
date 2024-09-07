```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

class ForecastModel:
    def __init__(self):
        self.model = LinearRegression()

    def loadData(self, filename):
        self.data = pd.read_csv(filename)
        self.data.dropna(inplace=True)

    def preprocessData(self):
        self.X = self.data[['market cap', 'P/E', 'price', 'change', 'volume']].values
        self.y = self.data['price'].values

    def trainModel(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=0)
        self.model.fit(X_train, y_train)
        self.y_pred = self.model.predict(X_test)

    def predict(self, X_new):
        return self.model.predict(X_new)

if __name__ == "__main__":
    forecast_model = ForecastModel()
    forecast_model.loadData('data/nyse_stocks.csv')
    forecast_model.preprocessData()
    forecast_model.trainModel()
```