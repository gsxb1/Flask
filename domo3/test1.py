import pymysql


class Database:
    def __init__(self):
        # 在初始化方法中创建数据库连接
        self.db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
        self.cursor = self.db.cursor()
        self.cursor.execute("USE login")
    # 创建以名字为表名的数据表
    def Factory_function(self, sql):
        def _(self, name):
            # 关闭事务
            self.db.commit()
            # 关闭连接
            self.db.close()

    # 为数据表插入数据
    # 账户名，书名，作者
    def insert_data(self, name, book, author):
        db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
        cursor = db.cursor()
        cursor.execute("use login")
        # 将表名直接嵌入到 SQL 查询中
        sql = f"insert into {name}(book, author, quantity) values('{book}', '{author}', 1);"
        cursor.execute(sql)
        # 关闭事务
        db.commit()
        # 关闭连接
        db.close()
name = None
sql = f"CREATE TABLE if not exists {name} (book VARCHAR(20), author VARCHAR(20), quantity INT)"
a = Database()
i = a.Factory_function(sql)
i("小兰")
# a.Add_Data_Table("小兰")
# a.insert_data("小兰", "活着", "余华")
# a.Delete_data("姚昊", "活着")
# a.login("小兰", "789546")
# a.query(0, "login")