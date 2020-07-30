#Kaitlyn Friden 3/11/2020
#This is a RESTful endpoint where another API is used where a world clock tells the time of day and timezone as well as other data points
#Flask is used to create the simple website 


from flask import Flask, render_template, request, json
import requests

app = Flask(__name__)

@app.route("/time", methods=['POST'])
def time():
    #The method requests.get calls the api which is the response
    response = requests.get("http://worldclockapi.com/api/json/est/now")
    #The response is called which returns the name of the timezone from the json data from the api
    return response.json()['timeZoneName']

    #return render_template("time.html")

@app.route("/")
def index():
    return render_template('index1.html')


if __name__ == '__main__':
    app.run(debug=True)