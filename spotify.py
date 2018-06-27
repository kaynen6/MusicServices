import requests, json, keys

client_id = keys.spot_clientid
client_secret = keys.spot_secret


headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    }
params = {"grant_type":"client_credentials"}
url = "https://accounts.spotify.com/api/token"

r = requests.request("POST", url, auth=(client_id, client_secret),headers=headers, params = params)


if r.status_code == 200:
    print(r.json)
    toke= r.json.get["access_token"]

    with open(keys.path, "r") as f:
        