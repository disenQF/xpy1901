# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider


class MvSpider(RedisCrawlSpider):
    name = 'mv'
    allowed_domains = ['meinv.hk']

    # 爬虫的开始位置从redis的队列中读取
    redis_key = 'mv:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'http://www.meinv.hk/\?p=\d+'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.css('.post h1::text').get()
        item['image_urls'] = response.css('.post-content img::attr(src)').extract()
        yield item
