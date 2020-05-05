from flask import Flask, request
import requests, json

app = Flask(__name__)

token = "c8f6dab6ea016097d9c7c323219d4875a6fd5a7030ebf35d4c86b51d2b85a406"

HEADERS = {
            "Authorization": "Bearer %s" % token,
            }

API_URL = 'https://api.lifx.com/v1/lights/all'
color = 'white'
powerState = 'off'


@app.route("/light_off", methods=["GET"])
def light_off():
        payload = {
                "power":"off"
        }
        response = requests.put(\
                'https://api.lifx.com/v1/lights/all/state', \
                data=payload, headers=HEADERS)
        print(response)
        return f"light response: {response.text}"
@app.route("/light_on", methods=["GET"])

def light_on():
        payload = {
                "power":"on"
        }
        response = requests.put(\
                'https://api.lifx.com/v1/lights/all/state', \
                data=payload, headers=HEADERS)
        print(response)
        return f"light response: {response}"
@app.route("/", methods=["GET"])
def root():
    return "hello world"
    
if __name__ == "__main__":
    light_on()
    light_off()
    light_on()

    app.run(host='192.168.1.129')
