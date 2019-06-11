# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 在 items.py文件中，定义不同页面提取不同数据的item类
# item类，封装成了字典的类

import scrapy


# 任务1： python元类 orm
# 任务2： python自省相关的函数
class ThumbItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()  # 用户名
    info_url = scrapy.Field()  # 个人主页地址
    img_url = scrapy.Field()  # 图片地址
    width = scrapy.Field()   # 图片宽度
    height = scrapy.Field()  # 图片高度


class XHItem(scrapy.Item):
    uid = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    name = scrapy.Field()


