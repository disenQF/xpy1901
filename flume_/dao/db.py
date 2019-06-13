import pymysql
from pymysql.cursors import DictCursor

from dao import DB_CONFIG


class DB(object):
    def __init__(self):
        self.conn = pymysql.Connect(**DB_CONFIG)
        self.is_inited = False

    def init_db(self):
        # 判断是否已创建表
        if self.is_inited: return

        with self.conn as c:
            c.execute("""
            CREATE TABLE log(
                ip CHAR(32),
                upload_time VARCHAR(50),
                level VARCHAR(10),
                message TEXT,
                filepath VARCHAR(100),
                lineno VARCHAR(6)
            )
            """)

        # SQL的三大语言分类： DDL, DML, DCL
        self.is_inited = True

    def __enter__(self):
        # 当类的实例对象使用with且进入上下文环境时调用
        # 返回cursor的对象
        return self.conn.cursor(cursor=DictCursor)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 退出上下文环境时调用
        # 1) 如果没有异常，则提交事务
        # 2) 如果有异常时，则上传日志且回滚事务
        # [重要提示]  如果有异常，且返回True时，表示异常在此函数中终结，
        #             反之返回False时，异常继续被抛出, 如果外部不处理异常，则会中断程序
        if exc_type is None:
            self.conn.commit()  # 没有异常
        else:
            self.conn.rollback()  # 有异常，则回滚事务

        return True

