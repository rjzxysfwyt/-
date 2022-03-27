from pymysql import connect
from config import *

class DB(object):
    """数据库管理类"""

    def __init__(self):
        self.conn=connect(host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS,
                charset='utf-8')
        #获取游标
        self.cursor=self.conn.cursor()

    def close(self):
        """释放数据库资源"""
        self.cursor.close()
        self.conn.close()


