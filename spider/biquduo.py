# -*- coding: utf-8 -*-
import scrapy


class BiquduoSpider(scrapy.Spider):
    name = 'biquduo'
    allowed_domains = ['biquduo.com']
    start_urls = ['www.biquduo.com/biquge/54_54410/']

    def parse(self, response):
        pass
