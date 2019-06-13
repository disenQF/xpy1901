from dao.base import BaseDao


class LogDao(BaseDao):
    def __init__(self):
        super().__init__()
        # self.db.init_db()
        self.table_name = 'log'

    def save(self, **data):
        # 验证data字典的key是否为self.table_name指定表的字段名
       super().save(self.table_name, **data)

    def query(self, page=1, size=20):
        return super().query(self.table_name,
                             'ip', 'upload_time', 'message')