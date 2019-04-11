#poster
# encoding=utf-8
import os
from io import BytesIO
import requests
from bs4 import BeautifulSoup
import time
from PIL import Image
import re
import csv
import pandas as pd

index = 0
ptitle = ''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def get_images(name, no, type):
	global index
	global ptitle

	if not os.path.exists("./images/" + name + '/' + type):
		os.makedirs("./images/" + name + '/' + type)

	url = 'https://www.imdb.com/name/'+no+'/mediaindex?refine=poster&ref_=nmmi_ref_pos' 
	html = BeautifulSoup(requests.get(url, headers=headers).text, features="html.parser")
	imgs = html.find('div', {'class', 'media_index_thumb_list'}).find_all('a')
	for link in imgs:
		img = re.sub(r'V1(\S*).jpg','V1.jpg', link.find('img').get('src'))
		txt = link.find('img').get('alt')
		print(txt)
		time.sleep(0.1)
		try:
			r = requests.get(img, timeout=5, stream=True)
			tmpIm = BytesIO(r.content)
			im = Image.open(tmpIm)
			print(im.size[0])
			if(im.size[0]<500 or im.size[0]>1200):
				print('inappropriate')
				continue
		except Exception as e:
			print(e)
			continue
		
		with open('./images/' + name + '/' + type + '/' + str(index) + ".jpg", 'wb') as jpg:
			print("正在抓取第%s条数据" % index)
			jpg.write(r.content)
			ptitle += txt+'|'
			index += 1

	data = pd.read_csv('star.csv', encoding='utf-8')
	data.tail(1)[type] = str(index)
	data.tail(1)[type+'t'] = ptitle
	print(data.tail(1)[type])
	data.to_csv('star.csv', header=True, index=False, encoding='utf-8')

#get_images('Jason Statham', 'nm0005458', 'poster')
get_images('Jason Statham', 'nm0005458', 'still')
