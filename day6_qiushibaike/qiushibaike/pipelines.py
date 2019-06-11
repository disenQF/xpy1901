# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from csv import DictWriter

# 将spider爬虫的解析后的数据进一步处理
# 将item数据写入文件或数据库中
class QiushibaikePipeline(object):
    def __init__(self):
        self.filename = 'qb.csv'
        self.fieldnames = ('name', 'info_url', 'img', 'content')
        self.is_existsed = os.path.exists(self.filename)

    def process_item(self, item, spider):
        with open(self.filename, 'a') as file:
            writer = DictWriter(file, self.fieldnames)

            # 如果文件第一次使用，则写入标题行
            if not self.is_existsed:
                writer.writeheader()
                self.is_existsed = True

            writer.writerow(item)
        return item
