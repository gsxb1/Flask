import pymysql

class Database:
    def __init__(self):
        # 在初始化方法中创建数据库连接
        self.db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
        self.cursor = self.db.cursor()
        self.cursor.execute("USE login")

    def close_connection(self):
        # 在单独的方法中关闭数据库连接
        self.db.close()

    def execute_query(self, sql):
        # 单独的方法用于执行 SQL 查询，并返回结果
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def execute_update(self, sql):
        # 单独的方法用于执行 SQL 更新（插入、删除等）操作
        self.cursor.execute(sql)
        self.db.commit()

    def Add_Data_Table(self, name):
        # 创建以名字为表名的数据表
        sql = f"CREATE TABLE IF NOT EXISTS {name} (book VARCHAR(20), author VARCHAR(20), quantity INT)"
        self.execute_update(sql)

    def insert_data(self, name, book, author):
        # 为数据表插入数据
        sql = f"INSERT INTO {name}(book, author, quantity) VALUES ('{book}', '{author}', 1);"
        self.execute_update(sql)

    def Delete_data(self, name, book):
        # 删除数据表中的数据
        sql = f"DELETE FROM {name} WHERE book='{book}' LIMIT 1;"
        self.execute_update(sql)

    def login(self, name, password):
        # 创建用户名密码的登录表，可以添加数据
        sql = f"CREATE TABLE IF NOT EXISTS login (name VARCHAR(20), password VARCHAR(20))"
        self.execute_update(sql)

        sql = f"INSERT INTO login(name, password) VALUES ('{name}', '{password}');"
        self.execute_update(sql)

    def query(self, __, table):
        # 查询数据表或列出所有表
        if __ == 0:
            return self.execute_query(f"SELECT * FROM {table};")
        else:
            return self.execute_query("SHOW TABLES;")
