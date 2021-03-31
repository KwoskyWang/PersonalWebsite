import scrapy
import json

from ..items import NovelItem, NovelContent


class NovelSpider(scrapy.Spider):
    name = 'lwzx'
    allowed_domains = ["www.biquduo.com"]
    start_urls = [
        "https://www.biquduo.com/biquge/54_54410/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]      # 按照'/'分割之后拿到倒数第二个字段
        for sel in response.xpath('//*[@id="list"]/dl/dd'):
            item = NovelItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['link'] = 'www.biquduo.com' + str(item.get('link')).split('\'')[-2]
            # print('标题是:' , title, '/n','链接是:www.biquduo.com/', link)
            yield item

# 读取网页的json文件
def getTheUrl():
    f = open('/Users/moooke/PycharmProjects/untitled2/spider/novel/novel/items.json', 'r', encoding='gbk')

    parsed_json = json.load(f)

    url_list = []

    for i in parsed_json["novel_items"]:
        url_list.append(i.get('link'))

    return url_list


class ContentSpider(scrapy.Spider):
    name = 'content'
    allowed_domains = ["www.biquduo.com"]
    start_urls = ["https://m.biquduo.com/biquge/54_54410/c23414473.html",
                  "https://m.biquduo.com/biquge/54_54410/c23414473_2.html"]

    def parse(self, response):
        # filename = response.url.split("/")[-2]      # 按照'/'分割之后拿到倒数第二个字段
        se = 0
        for sel in response.xpath('//*[@id="nr1"]'):
            se += 1
            item = NovelContent()
            item['title'] = se
            item['content'] = sel.extract()
            # print('标题是:' , title, '/n','链接是:www.biquduo.com/', link)
            yield item


