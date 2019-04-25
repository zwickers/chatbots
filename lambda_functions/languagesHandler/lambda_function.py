import json
import requests

def lambda_handler(event, context):
    country = event["currentIntent"]["slots"]["Country"].title()
    endpoint = "https://restcountries.eu/rest/v2/name/" + country
    my_request = requests.get(endpoint)
    languages = my_request.json()[0]['languages']
    resp = ''
    if len(languages) == 1:
        resp = "In " + country + ", they speak " + languages[0]['name'] + "."
    else:
        resp = "In " + country + ", they speak "
        for i in range(len(languages)):
            if i != len(languages) - 1:
                resp += (languages[i]['name'] + ', ')
            else:
                resp += ('and ' + languages[i]['name'] + '.')
    response = {
                "dialogAction":
                    {
                     "fulfillmentState":"Fulfilled",
                     "type":"Close",
                     "message":
                        {
                          "contentType":"PlainText",
                          "content": resp
                        }
                    }
                }
    return response
