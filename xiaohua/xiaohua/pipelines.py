# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from xiaohua.items import ThumbItem
import pymysql
from xiaohua import settings


class XiaohuaPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(**settings.DB_CONFIG)

    def process_item(self, item, spider):
        if isinstance(item, ThumbItem):
            print('列表页面的数据')
            sql = 'INSERT INTO thumb_item(id, name, info_url, img_url, width, height) ' \
                  'values ( %(id)s, %(name)s,  %(info_url)s, %(img_url)s, %(width)s, %(height)s)'

        else:
            print('详情页面的数据')
            sql = 'insert into item_info(uid, img_url) ' \
                  'values(%(uid)s, %(img_url)s)'

        # 将item数据保存到数据库中
        with self.conn as c:

            c.execute(sql, args=dict(item))

        self.conn.commit()

        return item
