import requests

#create function find to retrieve location
def find(gameID):

    #make GET to endpoint, convert data into a JSON object
    response = requests.get(f"https://www.geoguessr.com/api/v3/games/{gameID}")
    obj = response.json()

    #parse the JSON for needed info which is the current round and the coords
    round = obj['round']
    lat = (obj["rounds"][round - 1]["lat"]) 
    lng = (obj["rounds"][round - 1]["lng"])

    #format coords into returnable value
    coords = (str(lat), str(lng))

    #now we take the coordinates and use a coords -> location api, we need a user agent header for this request
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }

    #make the GET and create another JSON obj
    response2 = requests.get("https://api.opencagedata.com/geocode/v1/json?q=" + str(lat) + "+" + str(lng) + "&key=03c48dae07364cabb7f121d8c1519492", headers=  headers)
    obj2 = response2.json()

    #parse and return the formatted final location
    formattedLocation = (obj2["results"][0]["formatted"])
    return [formattedLocation, coords]
