
# coding: utf-8

# In[1]:

import requests
import json
import keys
from requests.auth import HTTPBasicAuth


# In[2]:
## init user config from keys.py
username = keys.nap_username
password = keys.nap_password
api_key = keys.nap_api_key
api_secret = keys.nap_api_secret
path = keys.path

payload = {"username": username,"password": password, "grant_type":"password"}
r = requests.post("https://api.napster.com/oauth/token", auth=HTTPBasicAuth(api_key, api_secret), data = payload)


# In[3]:

r.text


# In[4]:

r.json()


# In[5]:


json.dumps(r.json())


# In[6]:

r.json().get("access_token")


# In[7]:

r.json().get("refresh_token")


# In[8]:

if r.status_code == 200:
    access_token = r.json().get("access_token")
    refresh_token = r.json().get("refresh_token") 
    life = r.json().get("expires_in")


# In[9]:

access_token
refresh_token
life


# In[10]:

headers = {"Authorization": "Bearer " +str(access_token)}
r = requests.get("https://api.napster.com/v2.2/me/account", headers=headers)


# In[11]:

r.text


# In[12]:

headers = {"Authorization": "Bearer "+str(access_token)}
r = requests.get("https://api.napster.com/v2.2/me/library/artists?limit=200", headers=headers)


# In[13]:

r.json()


# In[14]:

with open(keys.path, 'w+') as f:
    for artist in r.json().get("artists"):
        #print artist.get("name")
        artist["name"].strip('"')
        json.dump(artist.get("name"),f)
        f.write("\n")


# In[15]:

r = requests.get("https://api.napster.com/v2.2/me/library/artists?limit=200&offset=200", headers=headers)


# In[16]:

with open(keys.path, 'a+') as f:
    for artist in r.json().get("artists"):
        #print artist.get("name")
        artist["name"].strip('"')
        json.dump(artist.get("name"),f)
        f.write("\n")


# In[ ]:




# In[ ]:



