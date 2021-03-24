from flask import Flask, redirect, url_for, render_template, request, jsonify, g, session, flash
from flask_restful import Api
import requests
from discord import Webhook, RequestsWebhookAdapter
import sqlite3
import time
from multiprocessing import Process
from flask import Flask
import json


app = Flask(__name__)
app.secret_key = '6969691'
api = Api(app)


@app.route('/', methods=['GET'])
def api2():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
        ip = request.remote_addr
        loc = requests.get(f"http://ip-api.com/json/{ip}?fields=17")
        js = loc.json()
        country = (js["country"])
        city = (js["city"])
        print(city)
        url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={country}+{city}+grilled+cheese+restaurant&num=10"
        headers = {
            'x-rapidapi-key': "",
            'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        dict1 = json.loads(response.text)
        bob = dict1["results"]
        links = []
        for x in bob:
            b = (x["link"])
            links.append(b)
        final = links
        return render_template('grilled.html', result=final, title=title)
    else:
        ip = request.remote_addr
        loc = requests.get(f"http://ip-api.com/json/{ip}?fields=17")
        js = loc.json()
        country = (js["country"])
        city = (js["city"])
        print(city)
        url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={country}+{city}+grilled+cheese+restaurant&num=10"
        headers = {
            'x-rapidapi-key': "",
            'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        dict1 = json.loads(response.text)
        bob = dict1["results"]
        links = []
        for x in bob:
            b = (x["link"])
            links.append(b)
        final = links
        return render_template('grilled.html', result=final, title=title)

if __name__ == "__main__":
    app.run(debug=True)
