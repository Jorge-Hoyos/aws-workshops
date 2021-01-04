#%%
import requests
import json
#%%
def lambda_handler(event, context):
    print("In lambda handler")
    x = requests.get('https://la1.api.riotgames.com/lol/match/v4/matchlists/by-account/ATlWVKkc0J7UeygcoMhGb4yfRjxlRQwEDE4_8bze2os37as?api_key=RGAPI-f67d3acd-3e0d-4186-aef9-810e81e90360').json
    print (x)
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Jorge Hoyos"
    }

    return resp
#%%
