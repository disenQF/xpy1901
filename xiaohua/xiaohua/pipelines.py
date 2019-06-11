# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

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
            """ --- item['images'] 数据 ---
            [{'checksum': 'eaa78c3a594254624a445c2e98534026',
             'path': 'full/78608ef7c530c70b9659dbe8b02d366c19ce6ac0.jpg',
             'url': 'http://www.521609.com/uploads/allimg/111020/11329353c0-1.jpg'}]
            """
            item['images'] = os.path.join(settings.IMAGES_STORE,
                                          item['images'][0].get('path'))
            sql = 'insert into item_info(uid, img_url) ' \
                  'values(%(uid)s, %(images)s)'

        # 将item数据保存到数据库中
        # python上下文,使用with关键字, 如果哪一个对象使用了with,
        # 则这个对象的类必须实现__enter__()和__exit__()两个函数。
        # __enter__()是进入上下文时调用的函数，一般返回相应的对象
        # __exit__(self, exc_type, exc_val, exc_tb)
        #               当对象退出上下文时调用的函数，用于回收资源
        with self.conn as c:

            # args可以是元组， 对应是sql语句中的 %s
            # 也可以是字典,  对应是sql语句中的 %(key)s
            c.execute(sql, args=dict(item))

        return item
