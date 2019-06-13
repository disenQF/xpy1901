from dao.db import DB


class BaseDao():
    def __init__(self):
        self.db = DB()

    def save(self, table, **data):
        sql = 'INSERT INTO %s(%s) VALUES(%s)'
        fields = ','.join([key for key in data.keys()])
        values = ','.join(['%%(%s)s' % key for key in data.keys()])
        insert_sql = sql % (table,
                            fields,
                            values)

        with self.db as c:
            c.execute(insert_sql, args=data)

    def query(self, table, *fields, page=1, size=20):
        # 分页查询
        # 任务3： 实现日志的分页查询（query()的实现和views的接口）
        args = (','.join(fields) if len(fields) > 0 else '*',  # 查询字段
                table,
                (page-1)*size,
                size)
        sql = 'select %s from %s limit %s, %s' % args
        with self.db as c:
            c.execute(sql)
            data = c.fetchall()

        return data
