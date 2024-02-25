#!/usr/bin/env python3

import requests
import json


########################################################################################################################################################

# Your user ID
userID = 0


# Your .robloSecurity key
robloSecurity = ''

########################################################################################################################################################


if (robloSecurity == ''):
    print("\n\nYou did not pass a RobloSecurity key.\nPaste it in the script, save file, then try again.\n")
    exit()


if (userID == '' or userID == 0):
    print("\n\nYou have not given your user ID.\nPaste it in the script, save file, then try again.\n")
    exit()




confirmed = 'no'

print("\n\nRBXKillAllFollowers - " + "\x1b[39;49;1m" + "github.com/splatert" + "\x1b[0m")

print("\n\n" + "\x1b[31;40;1m" + "! WARNING !" + "\x1b[0m")
print("This method uses the 'block user' function to clear out followers.")
print("\x1b[39;49;1m" + "Any roblox friends that follow you will be unfriended" + "\x1b[0m")
print("\n\nEnter OK to continue.")
print("\nEnter QUIT to quit the program.")

acknowledgement = input()
if (acknowledgement == 'QUIT' or acknowledgement == "quit" or acknowledgement == ""):
    exit()



session = requests.Session()
session.cookies['.ROBLOSECURITY'] = robloSecurity
session.headers['x-csrf-token'] = session.post('https://accountsettings.roblox.com/v1/users/1/block').headers['x-csrf-token']

followersCount = requests.get(f'https://friends.roblox.com/v1/users/{userID}/followers/count')
followers = requests.get(f'https://friends.roblox.com/v1/users/{userID}/followers?sortOrder=Asc&limit=100')





while followersCount.json()['count'] != 0:
    for i in followers.json()['data']:

        id = i['id']
        
        session.post(f'https://accountsettings.roblox.com/v1/users/{id}/block')
        session.post(f'https://accountsettings.roblox.com/v1/users/{id}/unblock')

        username = requests.get(f'https://friends.roblox.com/v1/metadata?targetUserId={id}').json()['userName']
        print(f'Removed: {username}')


    nextPageCursor = followers.json()['nextPageCursor']
    followers = requests.get(f'https://friends.roblox.com/v1/users/{userID}/followers?sortOrder=Asc&limit=100&cursor={nextPageCursor}')
    followersCount = requests.get(f'https://friends.roblox.com/v1/users/{userID}/followers/count')


session.post('https://accountsettings.roblox.com/v1/users/1/unblock')


print("\n\nAll followers have been removed.")