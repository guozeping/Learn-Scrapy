# -*- coding: utf-8 -*-
import scrapy


class DbbookspiderSpider(scrapy.Spider):
    name = 'dbbookspider'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        print(response.text)
