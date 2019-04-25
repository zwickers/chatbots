import json
import requests

def lambda_handler(event, context):
    country = event["currentIntent"]["slots"]["Country"].title()
    endpoint = "https://restcountries.eu/rest/v2/name/" + country
    my_request = requests.get(endpoint)
    capital = my_request.json()[0]['capital']
    response = {
                "dialogAction":
                    {
                     "fulfillmentState":"Fulfilled",
                     "type":"Close",
                     "message":
                        {
                          "contentType":"PlainText",
                          "content": "The capital of " + country + " is " + capital + "."
                        }
                    }
                }
    return response
