import os
import requests
from bs4 import BeautifulSoup
import time

index = 0
page = 0
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def get_images(name, no):
	global index
	global page
	
	print("第"+str(page+1)+"页")
	if not os.path.exists("./" + name):
		os.mkdir("./" + name)

	url = 'https://movie.douban.com/celebrity/'+no+'/photos/?type=C&start='+str(page*30)+'&sortby=like&size=a&subtype=a' 
	html = BeautifulSoup(requests.get(url, headers=headers).text, features="html.parser")
	cover = html.find_all('div',{'class', 'cover'})
	for img in cover:
		src = img.find('img').get('src').replace('/m/','/l/')
		time.sleep(0.1)
		try:
			r = requests.get(src, timeout=3)
		except Exception as e:
			print(e)
			continue
		
		with open('./' + name + '/' + str(index) + ".jpg", 'wb') as jpg:
			jpg.write(r.content)
			print("正在抓取第%s条数据" % index)
			index += 1
	page += 1

def iter_page(name, no, total):
	global page
	while page < total:
		get_images(name, no)

iter_page('Jason Statham', '1049484', 5)
