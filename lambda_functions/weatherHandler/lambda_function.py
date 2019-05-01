import json
import requests

def lambda_handler(event, context):
    
    location = event["currentIntent"]["slots"]["Location"].title()
    
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" \
    + location \
    + "&appid=04e23b8bee0999c2ae5feb407bf67c70&units=imperial")
    
    name = r.json()['name']
    fahr = r.json()['main']['temp']
    
    
    
    weather = r.json()['weather'][0]['main']
    
    
    response = {
                "dialogAction":
                    {
                     "fulfillmentState":"Fulfilled",
                     "type":"Close",
                     "message":
                        {
                          "contentType":"PlainText",
                          "content": "In " + name + ", it is " + str(fahr) + " degrees with " + weather
                        }
                    }
                }
    return response
