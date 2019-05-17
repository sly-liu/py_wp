
#profile
# encoding=utf-8
import os
import requests
from bs4 import BeautifulSoup
import csv
import time
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def get_profile():
	con = ''
	url = 'https://music.163.com/api/v1/resource/comments/A_DJ_1_2060617031'
	html = requests.get(url, headers=headers).json()
	for x in html['comments']:
		con += x['content']+'---------'
	print(con)


get_profile()
