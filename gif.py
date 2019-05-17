# python
import urllib.request
import json
import requests
from datetime import datetime 

a=datetime.now()
index=0
data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q=Catherine+Zeta+Jones&api_key=Gn6L4EOc0zrGNso2WcmRwipSPa3OWKX0&limit=5").read())
jsons = json.dumps(data, sort_keys=True, indent=4)
print (jsons)
for item in data['data']:
	original_mp4 = item['images']['original_mp4']['mp4']
	print(original_mp4)
	r = requests.get(original_mp4, timeout=1)
	index+=1
	with open('./'+str(index)+'.mp4', 'wb') as mp4:
		mp4.write(r.content)
		
b=datetime.now()
print((b-a).seconds)