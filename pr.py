#profile
# encoding=utf-8
import os
import requests
from bs4 import BeautifulSoup
import csv
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def get_profile(name, no, dno):
	
	if not os.path.exists("./" + name):
		os.mkdir("./" + name)

	dh = ['name', 'sex', 'state', 'birth', 'bio', 'quote', 'wallpaper','poster', 'postert', 'still', 'stillt', 'gif', 'gift', 'create_time']
	di = {'name': name}

	url = 'https://www.imdb.com/name/'+no+'/bio?ref_=nm_ov_bio_sm'
	durl = 'https://movie.douban.com/celebrity/'+dno

	html = BeautifulSoup(requests.get(url, headers=headers).text, features="html.parser")
	dhtml = BeautifulSoup(requests.get(durl, headers=headers).text, features="html.parser")
	img = dhtml.find('a', {'class', 'nbg'}).get('href')
	dsoda = dhtml.find('div', {'class', 'info'}).find_all('li')
	sex = dsoda[0].get_text().strip()
	di['sex'] = 'Actor' if(sex[-1]=="男") else 'Actress'
	try:
		r = requests.get(img, timeout=5)
		with open('./' + name + '/' + 'thumbnail.jpg', 'wb') as jpg:
			jpg.write(r.content)
	except Exception as e:
		print(e)

	soda = html.find_all('div',{'class', 'soda'})
	overview = html.find('table', id='overviewTable').find_all('tr')[0]

	di['bio'] = soda[0].get_text().strip().replace("\n", "").replace("'", "\\'")
	di['birth'] = overview.find('time').get_text().replace("\n", "")
	di['state'] = overview.find_all('a')[2].get_text()

	quotes = ''
	for quote in html.find('a', {'name': 'quotes'}).find_next_siblings('div',{'class', 'soda'}):
		quotes += quote.get_text().strip()+'|'

	di['quote'] = quotes[:-1].replace("'", "\\'")
	di['wallpaper'] = 'w'
	di['poster'] = 'p'
	di['postert'] = 'pt'
	di['still'] = 's'
	di['stillt'] = 'st'
	di['gif'] = 'g'
	di['gift'] = 'pt'
	di['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

	with open('star.csv', 'a', encoding='utf-8', newline='') as f:
		writer = csv.DictWriter(f, dh)
		writer.writeheader()
		writer.writerow(di)

get_profile('Leonardo DiCaprio', 'nm0000138', '1041029')
