# COMS 6156 Project: Facebook Messenger Chatbots

## Serverless Chatbot Instructions

The code for each lamdba function is present in the /lambda_functions folder. Simply copy and paste each of these into your Lambda development console for each intent.

Inside your Lex development console, create an intent for each Lambda function. To associate an intent with a Lambda funtion, go to Editor --> your_intent_name --> Fulfillment, click on AWS Lambda Function, and then select the Lambda function you want to associate with it from the dropdown menu.

Every Lambda function uses the python 'requests' library to make HTTP requests to various APIs. Lambda requires you to upload the source code for any libraries you import...
Compress the /lambda_dependencies folder into a zip file. For every single one of your Lambda functions, navigate to the code editor. In the dropdown menu below "Code entry type", select "Upload a .zip file", and then select the compressed /lambda_dependencies folder.

You will also need to setup a Facebook page, register your app with Facebook, and retrieve a webhook from the Facebook Developer Portal. The official Facebook tutorial explains how to do this here: https://developers.facebook.com/docs/messenger-platform/getting-started/

## Cloud Server Chatbot instructions
See privacy_policy.txt for privacy info.

Description of how to set up and run chatbot:
First, clone the repository into your local directory. Then, navigate to the /server_chatbot folder.
The chatbot.py code can be modified to suit the specific needs of your chatbot!
Our chatbot is configured with a bunch of pre-existing functionality!

Next, set up a heroku server from the CLI and push the code to Heroku

On the Facebook developer console, create a messenger application, and identify the required tokens.
Add these to the config of the Heroku server.

Now we will set up the Natural Language Processing with DialogFlow.
After creating a new application, identify the required tokens, and put that into the Heroku config.
Finally, create the intents that correspond to your desired chatbot!

Now that everything is set up, you can test your chatbot by sending a message to it and seeing the results!



