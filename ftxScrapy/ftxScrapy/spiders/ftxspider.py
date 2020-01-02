# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from lxml import etree
from bs4 import BeautifulSoup

class FtxspiderSpider(scrapy.Spider):
    name = 'ftxspider'
    allowed_domains = ['www.fang.com']
    start_urls = ['http://www.fang.com/']


    def parse(self, response):
        selector = Selector()
        page = selector.xpath('//*html')
        print(page)


