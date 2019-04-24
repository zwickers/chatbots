import json

def lambda_handler(event, context):
    name = event["currentIntent"]["slots"]["Name"].title()
    response = {
                "dialogAction":
                    {
                     "fulfillmentState":"Fulfilled",
                     "type":"Close",
                     "message":
                        {
                          "contentType":"PlainText",
                          "content": "Hello "+ name + ", nice to meet you!"
                        }
                    }
                }
    return response
