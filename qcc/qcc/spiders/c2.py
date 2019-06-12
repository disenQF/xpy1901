# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class C2Spider(CrawlSpider):
    name = 'c2'
    allowed_domains = ['www.qichacha.com']
    start_urls = ['https://www.qichacha.com/g_AH.html']

    rules = (
        Rule(LinkExtractor(restrict_css='.ma_h1'), callback='parse_info', follow=False),
        Rule(LinkExtractor(restrict_css='.pagination'), follow=True),
        Rule(LinkExtractor(restrict_css='.pills-after'), follow=True)
    )

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
