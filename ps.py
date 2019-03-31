import os
import requests
from bs4 import BeautifulSoup
import time

index = 0
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def get_images(name, no):
	global index
	
	if not os.path.exists("./" + name + '/poster'):
		os.mkdir("./" + name + '/poster')

	url = 'https://www.imdb.com/name/'+no+'/mediaindex?refine=poster&ref_=nmmi_ref_pos' 
	html = BeautifulSoup(requests.get(url, headers=headers).text, features="html.parser")
	imgs = html.find('div', {'class', 'media_index_thumb_list'}).find_all('a')
	for link in imgs:
		img = link.find('img').get('src').replace('_UX100_CR0,0,100,100_AL_', '_SY1000_CR0,0,631,1000_AL_')
		time.sleep(0.1)
		try:
			r = requests.get(img, timeout=3)
		except Exception as e:
			print(e)
			continue
		
		with open('./' + name + '/poster/' + str(index) + ".jpg", 'wb') as jpg:
			jpg.write(r.content)
			print("正在抓取第%s条数据" % index)
			index += 1

get_images('Jason Statham', 'nm0005458')
