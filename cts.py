import pymysql 
import csv
# 打开数据库连接
db = pymysql.connect("localhost","root","","star" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
with open('star.csv', newline='', encoding='utf-8') as f:
	reader = csv.reader(f)
	for index, row in enumerate(reader):
		print(row)
		args = tuple(row)
		print(args)
		if(index == 0):
			continue

		# SQL 插入语句
		# SQL 插入语句
		sql = "INSERT INTO gp_star(name,sex,state,birth,bio,quote,wallpaper,poster,postert,still,stillt,gif,gift,create_time) \
		       VALUES ('%s','%s','%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
		       args

		try:
		   # 执行sql语句
		   cursor.execute(sql)
		   # 提交到数据库执行
		   db.commit()
		   print('Success!')
		except:
		   # 如果发生错误则回滚
		   db.rollback()
		   print('Error!')
# 关闭数据库连接
db.close()
