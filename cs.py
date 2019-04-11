import csv
import pandas as pd

#读取
def read():
	with open('gpb.csv', newline='', encoding='utf-8') as f:
		reader = csv.reader(f)
		for row in reader:
			print(row)

#写入
def write():
	headers = ['name', 'age', 'loc']
	datas = [
		{'name':'Bob', 'age':23},
		{'name':'Jerry', 'age':18},
		{'name':'Tom', 'age':15}
	]
	row = {'name':'Bob'}
	row['age'] = 12
	row['loc'] = 'nc'
	with open('test.csv', 'a', newline='') as f:
		writer = csv.DictWriter(f, headers)
		writer.writeheader()
		for row in datas:
			writer.writerow(row)

#修改
def edit():
	data = pd.read_csv('test.csv',encoding='utf-8')
	data.head(1)[u'name'] = 'dylan2'
	print(data.head(1)[u'name'])
	print(data)
	# first_rows = data.head(1) 
	# first_rows[u'loc'] = 'beijing'
	# print(first_rows)
	# cols = data.columns 
	# print(cols)
	# dimensison = data.shape #返回数据的格式，数组，（行数，列数）
	# print(dimensison)
	# print(data.values[2:]) #返回底层的numpy数据
	# data[u'loc'] = 'beijing122'
	data.to_csv('test.csv', header=True, index=False, encoding='utf-8')