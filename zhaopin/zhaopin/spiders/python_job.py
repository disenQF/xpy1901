# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy import Request
from scrapy.http import HtmlResponse


"""
招聘网已被动态js反爬
 - 解决办法： Selenium实现下载中间件
"""

class PythonJobSpider(scrapy.Spider):
    name = 'job1'
    allowed_domains = ['sou.zhaopin.com']
    start_urls = ['https://sou.zhaopin.com/?jl=854&sf=0&st=0&kw=python&kt=3']
    start_page = 1

    def parse(self, response:HtmlResponse):
        # with open('zhaopin.html', 'wb') as file:
        #     file.write(response.body)
        #     print('下载成功')
        # 解析数据
        print('--->ok-->', response.url)
        time.sleep(1)

        # 发起下一页请求
        next_url = 'https://sou.zhaopin.com/?jl=854&sf=0&st=0&kw=python&kt=3&p=%s'
        self.start_page += 1
        yield Request(next_url % self.start_page)



