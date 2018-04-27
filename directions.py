from flask import Flask, request, redirect, render_template, url_for
from twilio.rest import Client
import requests


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sms", methods=["POST"])
def text():
    if request.method == 'POST':
        num = request.form['phone_number']
        to = request.form['whereTo']
        wfrom = request.form['whereFrom']

        API_KEY = 'AIzaSyAprfFcqZB3DGbEeHGlHC_MqEC-uQXnCBw'

        origin = '9+Nystrom+Trail,Matawan,NJ,USA'
        destination = 'Rutgers–New Brunswick,New Brunswick,NJ,USA'

        url = 'https://maps.googleapis.com/maps/api/directions/json?origin=' + origin + '&destination=' + destination + '&key='
        full_url = url+API_KEY
        directions_json = requests.get(full_url).json()
        temp = []
        print(to)
        print(wfrom)
        count = 1
        for i in directions_json['routes'][0]['legs'][0]['steps']:
            directions = (i['html_instructions']).replace("<b>", "").replace("</b>","")
            directions = directions.replace('<div style="font-size:0.9em">', ' ').replace('</div>','').replace('&nbsp;',' ')
            temp.append(str(count) + '. ' + directions + ' for '+ i['distance']['text']+"\n\n")
            count = count + 1
        res = ''.join(temp)
        print(res)

        account_sid = "AC58a4d2de362269e533d0255acda5fb81"
        auth_token = "d71831993dca13d138c044f94e374c14"
        client = Client(account_sid, auth_token)
        number = '+1' + num
        message = client.messages.create(
            number,
            body=res,
            from_="+17325921530"
        )
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)