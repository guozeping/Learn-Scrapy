# -*- coding: utf-8 -*-
import scrapy


class ExamplespiderSpider(scrapy.Spider):
    name = 'examplespider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
