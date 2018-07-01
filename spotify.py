import requests, json, keys

client_id = keys.spot_clientid
client_secret = keys.spot_secret


#get token from spotify
headers = {'Content-Type': "application/x-www-form-urlencoded"}
params = {"grant_type":"client_credentials"}
url = "https://accounts.spotify.com/api/token"

r = requests.request("POST", url, auth=(client_id, client_secret),headers=headers, params = params)


if r.status_code == 200:
    print(r.json())
    response = r.json()
    token = response.get("access_token")
    artists = []
    with open(keys.path, "r") as f:
        for line in f:
            artists.append(f.readline())
    ## search artist
    ids = []
    for artist in artists:
        artist = artist.replace(" ","+")
        artist = artist.strip("\n")
        artist = artist.strip('"')
        url = "https://api.spotify.com/v1/search"
        headers = {'Authorization': 'Bearer '+token}
        params =  {'q': artist, 'type': 'artist', 'limit': 1}
        r = requests.request("GET", url, headers= headers, params= params)
        response = r.json()
        # print(response['artists']['items'][0]['id'])
        try:
            ids.append(response['artists']['items'][0]['id'])
        except:
            print("Error adding ID from artist: {0}".format(artist))
        #print(ids)
    