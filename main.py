import requests
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/', methods=["POST", "GET"])
def get_price():
    if request.method == "POST":
        crypto_symbol = request.form.get('crypto')
        currencies = request.form.get('currency')
        parameters = {
            "fsym": crypto_symbol,
            "tsyms": currencies
        }

        response = requests.post(url="https://min-api.cryptocompare.com/data/price", params=parameters)
        print(json.dumps(response.json()))
        return render_template('index.html', crypto_symbol=crypto_symbol, result=response.json())
        # f"<h2>Price of {crypto_symbol}</h2>"\
        #        f"{json.dumps(response.json())}"


if __name__ == "__main__":
    app.run(debug=True)
