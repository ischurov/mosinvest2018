from flask import Flask, render_template
import requests

app = Flask(__name__)

app.debug = True

# Our code here
# Задача: написать "заглавную страницу"
# (/), которая будет отображать список
# всех показателей из датафрейма,
# получаемого из API


def get_data():
    r = requests.get(
        "https://apidata.mos.ru/v1/datasets/2462/rows",
        {'api_key': "409da9eedb996a27d999087244445209"})
    data = r.json()
    return data


@app.route('/')
def show_indicators():
    data = get_data()
    names = [item['Cells']['NameInInformationSource']
             for item in data]
    return render_template("indicators.html",
                           names=names)

# Problem 2:
# Написать обработчик адреса вида /index
# Который отображает таблицу для индикатора
# с номером index
# Например, /0 должен отображать первый индикатор
@app.route("/<int:index>")
def show_indicator(index):
    data = get_data()
    table = data[index]['Cells']['IndexValues']
    return render_template("indicator.html",
                           table=table)

if __name__ == "__main__":
    app.run()
