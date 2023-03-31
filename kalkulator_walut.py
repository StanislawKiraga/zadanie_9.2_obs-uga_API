import requests
import csv
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0]['rates']
headers = rates[0].keys()


@app.route('/home')
def home():
    return render_template('base.htm')


@app.route('/recalculate', methods=['GET', 'POST'])
def recalculate():
    if request.method == 'POST':
        
    
        
with open('/Users/amitrosz-wromac/Desktop/Kodilla/Flask/API/rates.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=headers, delimiter=';')
    writer.writeheader()
    writer.writerows(rates)


if __name__ == "__main__":
    app.run(debug=True)
           
