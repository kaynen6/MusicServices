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
    for artist in artists:
        artist = artist.replace(" ","%20")
        artist = artist.strip("\n")
        artist = artist.strip('"')
        print(artist)
        url = "https://api.spotify.com/v1/search"
        headers = {'Authorization': 'Bearer '+token}
        pararms =  {'q': artist, 'type': 'artist', 'market':'from_token'}
        r = requests.request("GET", url, headers= headers, params= params)
        print(r.json())