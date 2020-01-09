# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def parse(self, response):
        pass
