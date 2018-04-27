from flask import Flask
import requests
import json



API_KEY = 'AIzaSyAprfFcqZB3DGbEeHGlHC_MqEC-uQXnCBw'
directions_json = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=Chicago,IL&destination=Los+Angeles,CA&waypoints=Joplin,MO|Oklahoma+City,OK&key=' + API_KEY).json()
print(directions_json)