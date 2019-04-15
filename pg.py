#gif
import os
import requests
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import json

def get_gif(name):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
	url = 'http://api.giphy.com/v1/gifs/search?q='+name.replace(' ','-')+'&api_key=Gn6L4EOc0zrGNso2WcmRwipSPa3OWKX0&limit=15';
	index = 0
	gift = ''

	if not os.path.exists('./images/'+name):
		os.mkdir('./images/'+name)

	if not os.path.exists('./images/'+name+'/gif'):
		os.mkdir('./images/'+name+'/gif')

	response = requests.get(url)
	data = response.json()
	for item in data['data']:
		original_mp4 = item['images']['original_mp4']['mp4']
		preview_mp4 = item['images']['preview']['mp4']
		src = item['images']['original']['url']
		gift += (item['title']+'|')

		time.sleep(0.1)
		try:
			r = requests.get(src, timeout=5)
			r1 = requests.get(original_mp4, timeout=5)
			r2 = requests.get(preview_mp4, timeout=5)
		except Exception as e:
			print(e)
			continue
		
		with open('./images/'+name+'/gif/gif_' + str(index) + ".gif", 'wb') as gif:
			print("正在抓取第%s条数据" % index)
			gif.write(r.content)
			#index += 1

		with open('./images/'+name+'/gif/m_' + str(index) + ".mp4", 'wb') as mp4:
			print("正在抓取第%s条数据" % index)
			mp4.write(r1.content)
			#index += 1

		with open('./images/'+name+'/gif/s' + str(index) + ".mp4", 'wb') as smp4:
			print("正在抓取第%s条数据" % index)
			smp4.write(r2.content)
			index += 1

		data = pd.read_csv('star.csv', encoding='utf-8')
		data.tail(1)[u'gif'] = str(index)
		data.tail(1)[u'gift'] = gift
		data.to_csv('star.csv', header=True, index=False, encoding='utf-8')

get_gif('Leonardo DiCaprio')