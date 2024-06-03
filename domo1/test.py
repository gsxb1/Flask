import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
cursor = db.cursor()
cursor.execute("use test")
cursor.execute("delete from sports where id=10;")
db.commit()
db.close()