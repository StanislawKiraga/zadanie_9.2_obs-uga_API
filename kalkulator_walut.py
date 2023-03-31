import requests
import csv
from flask import Flask, render_template, request


def get_data_from_nbp():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()
    rates = data[0]['rates']
    return rates


def export_data_to_csv(data, file_name='data.csv'):
    with open(file_name) as f:
        writer = csv.DictWriter(f)
        writer.writerows(data)


def calculate(data, amount, currency):
    rate = [d for d in data if d["code"] == currency][0]["ask"]
    return amount * rate

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculator():
    data = get_data_from_nbp()

    if request.method == 'POST':
        currency = request.form['currency']
        amount = request.form['amount']
        amount = float(amount)
        result = calculate(data, amount, currency)
        return render_template('base.htm', result=result, data=data)
    
    return render_template('base.htm', result=None, data=data)
    

if __name__ == '__main__':
    app.run(debug=True)


