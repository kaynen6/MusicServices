import requests, json, keys

client_id = keys.spot_clientid
client_secret = keys.spot_secret


#get token from spotify
print("Getting Access to Spotify Account.")
headers = {'Content-Type': "application/x-www-form-urlencoded"}
params = {"grant_type":"client_credentials"}
url = "https://accounts.spotify.com/api/token"

r = requests.request("POST", url, auth=(client_id, client_secret),headers=headers, params = params)


if r.status_code == 200:
    response = r.json()
    token = response.get("access_token")
    print(token)
    artists = []
    print("Accessing napster artist file.")
    with open(keys.path, "r") as f:
        for line in f:
            artists.append(f.readline())
    ## search artist
    artistDict = {}
    print("Fetching Spotify IDs for each artist in Napster Library.")
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
        if response:
            try:
                artistDict[response['artists']['items'][0]['name']]= {'id': response['artists']['items'][0]['id']}
            except:
                print("Error adding ID from artist: {0}".format(artist))
            #print(ids)
    # get albums for each artist
    print("Fetching Albums for each artist.")
    for artist in artistDict:
        artistDict[artist]["albums"] = []
        url = "https://api.spotify.com/v1/artists/{0}/albums".format(artistDict[artist]['id'])
        headers = {'Authorization': 'Bearer '+token}
        params = {'include_groups': 'album', 'market': 'US'}
        r = requests.request("GET", url, headers= headers, params= params)
        response = r.json()
        for album in response['items']:
             artistDict[artist]["albums"].append(album['id'])
        ## add albums to user library
        url = "https://api.spotify.com/v1/me/albums?"
        params = {'ids': []}
        headers['Content-Type'] = 'application/json'
        for i in range(0,len(artistDict[artist]["albums"])):
            params['ids'].append(artistDict[artist]["albums"][i]+',')
        r = requests.request('PUT', url, headers = headers, params = params)
        if r.status_code == 201:
            print("Successfully added albums to library from {0}.".format(artist))
        else: print("Adding Albums Failure")

