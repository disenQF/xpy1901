# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium.webdriver import Chrome

class ZhaopinSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhaopinDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def __init__(self):
        self.driver_path = '/Users/apple/drivers/chromedriver'
        self.browser = Chrome(executable_path=self.driver_path)
        self.firsted = True


    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        # 可以实现以下功能：
        #  1. 设置请求request对象的请求头或cookies以及代理
        #  2. 如果请求是动态js,则由selenium来请求，并封装成response对象
        self.browser.get(request.url)

        # 第一次进入页面时，点击 "知道了"
        if self.firsted:
            ok_btn = self.browser.find_element_by_class_name('risk-warning__content').find_element_by_tag_name('button')
            ok_btn.click()
            self.firsted = False

        # 循环滚动
        for i in range(1000, 15000, 500):
            self.browser.execute_script("var q = document.documentElement.scrollTop= %s" % i)
            time.sleep(0.5)

        # 获取网页的源码
        html: str = self.browser.page_source  # 字符串str类型

        # 封装成HtmlResponse对象，并返回response
        return HtmlResponse(request.url,
                            body=html.encode(encoding='utf-8'))

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
