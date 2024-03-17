from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def root():
    return "TUGAS1_1202210087_1202213156"

@app.route('/drink')
def drink():
    url = "https://beverages-and-desserts.p.rapidapi.com/beverages"

    headers = {
        "X-RapidAPI-Key": "18ad8afa11msh01f3a546cb9a2adp1f9136jsn0a5bc30f2622",
        "X-RapidAPI-Host": "beverages-and-desserts.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    drink = response.json()

    return render_template('drink.html', data1=drink)


@app.route('/food')
def food():
    url = "https://burgers-hub.p.rapidapi.com/burgers"

    headers = {
        "X-RapidAPI-Key": "18ad8afa11msh01f3a546cb9a2adp1f9136jsn0a5bc30f2622",
        "X-RapidAPI-Host": "burgers-hub.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    food = response.json()

    return render_template('food.html', data2=food)

if __name__ == '__main__':
    app.run(debug=True)
