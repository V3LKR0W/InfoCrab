''' 
Name: InfoCrab
Author: @V3LKR0W - Crabber.net | Twitter.com | Github.com
Date: 2/14/2021
'''
# [Imports]

import crabber, requests, json, time, wikipedia
from keys import *

# [Settings]

api = crabber.API(api_key=Keys['Key'], access_token=Keys['Access']) # API Initialization
global last_content
Settings = {
    'last_content' : '', # The last molt's content that the bot grabbed.
    'ids': [], # A list containing all posts ID's that have been answered by the bot
    'username': api.get_current_user().username, # Pretty obvious grabs the bot's username
    'refresh_time': 10, # Dont wanna spam the server with too many requests.
}


# [Bot functions]

while True:
    molts = api.get_molts_mentioning(Settings['username'])
    for p in molts:
        try:
            if p.content is not Settings['last_content'] and int(p.id) not in Settings['ids']:
                poster = api.get_crab(p.author.id)
                question = p.content.replace(f'@{Settings["username"]}','')
                answer = wikipedia.summary(question, sentences=1) 
                p.reply(answer)
                last_content = p.content
                Settings['ids'].append(int(p.id))
            else:
                pass
        except Exception:
            p.reply('error: you must be more specific with your queries young padwan. ')
    
    time.sleep(Settings['refresh_time'])
    