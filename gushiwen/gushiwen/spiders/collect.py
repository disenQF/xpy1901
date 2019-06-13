# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, FormRequest
from code_api import ydm

class CollectSpider(scrapy.Spider):
    name = 'collect'
    allowed_domains = ['so.gushiwen.org']

    def start_requests(self):
        # 第一次获取验证码
        code_url = 'https://so.gushiwen.org/RandCode.ashx'
        yield Request(code_url, callback=self.parse_code)

    def parse_code(self, response):
        # 保存验证码
        with open('code.png', 'wb') as f:
            f.write(response.body)

        # 执行云打码的API,获取图片验证码的字符串
        code = ydm.get_code('code.png')

        login_url = 'https://so.gushiwen.org/user/login.aspx'
        form_data = {
            'email': '610039018@qq.com',
            'pwd': 'disen8888',
            'code': code,
        }

        yield FormRequest(login_url,
                          formdata=form_data)

    def parse(self, response):

        cont_nodes = response.css('.sons>.cont')
        for cont_node in cont_nodes:
            item = {}
            item['title'] = cont_node.xpath('./p[1]//text()').get()
            item['year_name'], item['author'] = cont_node.xpath('./p[2]/a/text()').extract()
            item['content'] = cont_node.xpath('./div[last()]//text()').extract_first()

            yield item


if __name__ == '__main__':
    from lxml import etree

    with open('/Users/apple/PycharmProjects/xpy1901/gushiwen/c.html', 'r') as f:
        html = f.read()

    root = etree.HTML(html)
    cont_nodes = root.xpath('//div[@class="sons"]/div[@class="cont"]')
    for cont_node in cont_nodes:
        item = {}
        item['title'] = cont_node.xpath('./p[1]//text()')
        item['year_name'], item['author']= cont_node.xpath('./p[2]/a/text()')
        item['content'] = cont_node.xpath('./div[last()]//text()')

        print(item)
