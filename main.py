import requests
import json
import urllib 


headers = {
    "Content-Type": "application/json"
}

params = {
    "token":"", # Your slack token
    "channel": event["channel_id"]
}
    
def get_user():
    
    requests.post(
        'https://slack.com/api/conversations.join',
        headers=headers,params=params
        )
        
    r = (requests.get("https://slack.com/api/users.list",headers=headers,params= params)).json()
    user_id_list = '{}'.format(','.join({user["id"] for user in r["members"] if not user["is_bot"]}))
    return user_id_list

def invite_user():
    
    params["users"] = get_user()
        
    requests.post(
        "https://slack.com/api/conversations.invite",
        headers=headers,params=params
        )

invite_user()