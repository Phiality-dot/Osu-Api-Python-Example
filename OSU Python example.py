import requests
import json
def getbmap():
    bmap = int(input("insert beatmap id: "))
    url = 'https://osu.ppy.sh/api/get_beatmaps'
    keysandsuch = {
    'k': 'XXXXXX',
    'b': bmap
    }

    response = requests.get(url, params=keysandsuch)
    print("Beatmap/Song name is " + json.loads(response.text)[0]['title'])
    print("Beatmap creator is " + json.loads(response.text)[0]['creator'])
    print("Song Artist is " + json.loads(response.text)[0]['artist'])
    input("enter to quit")
def getuser():
    uid = int(input("insert user id: "))
    url = 'https://osu.ppy.sh/api/get_user'
    keysandsuch = {
    'k': 'XXXXXXX',
    'u': uid
    }

    response = requests.get(url, params=keysandsuch)
    print("Username is " + json.loads(response.text)[0]['username'])
    print("User accuracy is " + json.loads(response.text)[0]['accuracy'])
    print("User level is " + json.loads(response.text)[0]['level'])
    print("User country is " + json.loads(response.text)[0]['country'])
    input("enter to quit")
inp = int(input("1 for beatmaps, 2 for users: "))
if inp == 1:
    getbmap()
elif inp == 2:
    getuser()
else:
    print("error!")
    input("enter to quit")

