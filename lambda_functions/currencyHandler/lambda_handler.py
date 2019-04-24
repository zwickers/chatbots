import json
import requests

def lambda_handler(event, context):
    country = event["currentIntent"]["slots"]["Country"].title()
    endpoint = "https://restcountries.eu/rest/v2/name/" + country
    my_request = requests.get(endpoint)
    currency_name = my_request.json()[0]['currencies'][0]['name']
    response = {
                "dialogAction":
                    {
                     "fulfillmentState":"Fulfilled",
                     "type":"Close",
                     "message":
                        {
                          "contentType":"PlainText",
                          "content": country + " uses the " + currency_name + "."
                        }
                    }
                }
    return response
