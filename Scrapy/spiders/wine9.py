# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest, Request


class Wine9Spider(scrapy.Spider):
    name = 'wine9'
    allowed_domains = ['http://127.0.0.1']
    # start_urls = ['http://www.wine9.com/']

    def start_requests(self):
        param = {'username': '13316588977', 'password': 'Xiadong90'}
        yield Request(url='http://127.0.0.1/index.php', method='POST', callback=self.parse)
        # yield FormRequest('http://127.0.0.1/index.php', formdata=param, callback=self.parse)
        # yield Request(url='http://www.wine9.com/user.php?a=login', callback=self.login)

    def parse(self, response):
        print(response)
        print(response.text)
        pass
