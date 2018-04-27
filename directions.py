from flask import Flask, request, redirect, render_template, url_for
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sms", methods=["POST"])
def text():
    if request.method == 'POST':
        to = request.form['whereTo']
        wfrom = request.form['whereFrom']
        API_KEY = 'AIzaSyAprfFcqZB3DGbEeHGlHC_MqEC-uQXnCBw'
        origin = '9+Nystrom+Trail,Matawan,NJ,USA'
        destination = 'Rutgers–New Brunswick,New Brunswick,NJ,USA'
        url = 'https://maps.googleapis.com/maps/api/directions/json?origin=' + origin + '&destination=' + destination + '&key='
        full_url = url+API_KEY
        print(full_url)
        directions_json = requests.get(full_url).json()
        temp = []

        print(to)
        print(wfrom)
        count = 1
        for i in directions_json['routes'][0]['legs'][0]['steps']:
            directions = (i['html_instructions']).replace("<b>", "").replace("</b>","")

            print(directions)
            temp.append((str(count)+".)  " + i['distance']['text'] + " "+i['html_instructions']).replace("<b>", "").replace("</b>","")+"\n\n")
            count = count + 1
            # print(i)
        print(temp)
    return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)