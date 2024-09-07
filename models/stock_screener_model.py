```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

class StockScreenerModel:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()

    def loadData(self, filepath):
        self.data = pd.read_csv(filepath)
        self.data.set_index('ticker', inplace=True)

    def preprocessData(self):
        self.data.fillna(self.data.mean(), inplace=True)
        self.data_scaled = self.scaler.fit_transform(self.data)

    def trainModel(self, n_clusters=10):
        self.model = KMeans(n_clusters=n_clusters, random_state=0)
        self.model.fit(self.data_scaled)

    def predict(self, ticker):
        if ticker in self.data.index:
            return self.model.predict(self.scaler.transform([self.data.loc[ticker]]))[0]
        else:
            return None

screener_model = StockScreenerModel()
screener_model.loadData('data/nyse_stocks.csv')
screener_model.preprocessData()
screener_model.trainModel()
```