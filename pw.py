#wallpaper
import os
import requests
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

index = 0
page = 0
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def get_images(name, no):
	global index
	global page
	
	print("第"+str(page+1)+"页")
	if not os.path.exists("./images/" + name + '/wallpaper'):
		os.mkdir("./images/" + name + '/wallpaper')

	url = 'https://movie.douban.com/celebrity/'+no+'/photos/?type=C&start='+str(page*30)+'&sortby=like&size=a&subtype=a' 
	html = BeautifulSoup(requests.get(url, headers=headers).text, features="html.parser")
	cover = html.find_all('div',{'class', 'cover'})
	for img in cover:
		src = img.find('img').get('src').replace('/m/','/l/')
		time.sleep(0.1)
		try:
			r = requests.get(src, timeout=5)
		except Exception as e:
			print(e)
			continue
		
		with open('./images/' + name + '/wallpaper/p_' + str(index) + ".jpg", 'wb') as jpg:
			print("正在抓取第%s条数据" % index)
			index += 1
	page += 1



def iter_page(name, no, total):
	global page
	global index
	while page < total:
		get_images(name, no)

	data = pd.read_csv('star.csv', encoding='utf-8')
	data.tail(1)[u'wallpaper'] = str(index)
	print(data.tail(1)[u'wallpaper'])
	data.to_csv('star.csv', header=True, index=False, encoding='utf-8')

#iter_page('Leonardo DiCaprio', '1041029', 3)
iter_page('Catherine Zeta Jones', '1056058', 3)
