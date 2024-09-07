```python
from flask import Flask, render_template, request, jsonify
import pandas as pd
from models.stock_screener_model import screener_model
from models.strategy_backtester_model import backtester_model
from models.forecast_model import forecast_model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/screener', methods=['GET', 'POST'])
def screener():
    if request.method == 'POST':
        data = request.get_json()
        results = screener_model(data)
        return jsonify(results)
    return render_template('screener.html')

@app.route('/backtester', methods=['GET', 'POST'])
def backtester():
    if request.method == 'POST':
        data = request.get_json()
        results = backtester_model(data)
        return jsonify(results)
    return render_template('backtester.html')

@app.route('/forecast', methods=['GET', 'POST'])
def forecast():
    if request.method == 'POST':
        data = request.get_json()
        results = forecast_model(data)
        return jsonify(results)
    return render_template('forecast.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```