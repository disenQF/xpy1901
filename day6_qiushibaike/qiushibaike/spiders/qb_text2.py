# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse

import base64

class QbTextSpider(scrapy.Spider):
    name = 'qb-text2'

    # allowed_domains 指定可以访问url资源的域名
    # 如果 一个请求的URL是http://login.qiushibaike.com/login.html,
    # 是否可被下载吗？
    allowed_domains = ['www.qiushibaike.com']

    #  start_urls爬虫入口的URL
    start_urls = ['http://www.qiushibaike.com/text/']

    def parse(self, response: HtmlResponse):
        # 下载之后的由engine调用，获取提取到的数据(数据解析),
        # 返回一个字典对象
        print(type(response))
        print('--->', response.url)

        item = {}
        # 返回List[<Selector>, ...]
        articles = response.css('.article')
        for article in articles:

            item['info_url'] = article.css('.author').xpath('./a/@href').get()
            item['name'] = article.css('.author').xpath('./a/img/@alt').get()
            item['img'] = article.css('.author').xpath('./a/img/@src').get()
            content = ''.join(article.css('.content').xpath('./span/text()').extract())

            item['content'] = base64.b16encode(content.encode(encoding='utf-8')).decode()

            yield item
        

        # 找出下一页的url
        next_url = response.css('.pagination').xpath('.//li[last()]/a/@href').get()
        # 发起下一页的请求
        yield Request('http://www.qiushibaike.com'+next_url,
                      callback=self.parse, priority=10, dont_filter=True)
