# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request


class CompanySpider(scrapy.Spider):
    name = 'company'
    allowed_domains = ['www.qichacha.com']
    start_urls = ['https://www.qichacha.com/g_AH.html']

    def parse(self, response):
        # 提取公司的名称和详情页面的url
        a_nodes = response.css('.ma_h1')
        for a_node in a_nodes:
            company = ''.join(re.findall(r'([\u4e00-\u9fa5]+)',
                                         a_node.extract()))
            company_url = "https://www.qichacha.com"+a_node.xpath('./@href').get()
            yield Request(company_url,
                          callback=self.parse_info,
                          meta={'company': company},
                          priority=10)


        # 任务1： 下一页

        # 任务2： 其它的省份的企业

    def parse_info(self, response):
        # 获取联系电话、邮箱,简介,地址,官网, 法定代表人, 成立日期
        item = {}
        item['name'] = response.css('h1').xpath('./text()').get()
        item['tel'] = response.css('.dcontent').xpath('./div[1]/span[1]/span[2]/span/text()').get()
        item['email'] = response.css('.dcontent').xpath('./div[2]/span[1]/span[2]/a/text()').get()
        item['address'] = response.css('.dcontent').xpath('./div[2]/span[3]/a/text()').get()
        item['url'] = response.css('.dcontent').xpath('./div[1]/span[3]/a/@href').get()
        item['boss_name'] = response.css('#sanbanBase').xpath('.//tr[6]/td[2]/text()').get()
        if item['boss_name'] is None:
            item['boss_name'] = response.css('.bname h2').xpath('./text()').get()

        item['create_time'] = response.css('#sanbanBase').xpath('.//tr[11]/td[4]/text()').get()
        if item['create_time'] is None:
            item['create_time'] = response.css('#Cominfo').xpath('./table[2]//tr[2]/td[4]/text()').get()
        yield item

