from dao.db import DB


class BaseDao():
    def __init__(self):
        self.db = DB()

    def save(self,table, **data):
        sql = 'insert into %s(%s) values(%s)'
        fields = ','.join([key for key in data.keys()])
        values = ','.join(['%%(%s)s' % key for key in data.keys()])
        insert_sql = sql % (table,
                            fields,
                            values)

        with self.db as c:
            c.execute(insert_sql, args=data)

    def query(self, table, page=1, size=20):
        # 分页查询
        pass