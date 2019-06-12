# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1001.html']

    rules = (
        # 详情页面的连接提取规则
        Rule(LinkExtractor(allow=r'/book/\d+/'),
             callback='parse_item', follow=False),

        # 分页连接的提取规则
        Rule(LinkExtractor(restrict_css='.pages'), follow=True),

        # 分类连接的提取规则
        Rule(LinkExtractor(r'/book/\d+\.html'), follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['name'] = response.css('.book-title>h1').xpath('./text()').get()
        item['img'] = response.css('.book-pic').xpath('.//img/@src').get()
        item['isbn'] = response.css('.book-details>table').xpath('.//tr[1]/td[2]/text()').get()
        item['publish_date'] = response.css('.book-details>table').xpath('.//tr[1]/td[4]/text()').get()
        item['pages'] = response.css('.book-details>table').xpath('.//tr[2]/td[4]/text()').get()

        # 任务1： 提取一级、二级和三级的分类名称，以逗号分隔存入catetype字段
        # 任务2： 将提取到的数据写入到数据库中
        return item
