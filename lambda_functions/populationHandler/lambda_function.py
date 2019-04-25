import json
import requests

def lambda_handler(event, context):
    country = event["currentIntent"]["slots"]["Country"].title()
    endpoint = "https://restcountries.eu/rest/v2/name/" + country
    my_request = requests.get(endpoint)
    pop = my_request.json()[0]['population']
    response = {
                "dialogAction":
                    {
                     "fulfillmentState":"Fulfilled",
                     "type":"Close",
                     "message":
                        {
                          "contentType":"PlainText",
                          "content": "The population of " + country + " is " + str(pop) + "."
                        }
                    }
                }
    return response
