# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from ..items import BiaoqingItem
from scrapy import Selector,Request


class BqSpider(CrawlSpider):
    name='bqspider'
    main_url="gaoxiaogif.com"
    allowed_domains=[main_url]
    start_urls=['http://www.gaoxiaogif.com/qqbiaoqing']
    def parse(self, response):
        s=Selector(response)
        item=BiaoqingItem()
        for i in s.xpath("//li//img"):
            item["image_url"]=i.xpath('@src').extract()
            yield item
        urls=s.xpath("//div[@class='lm-box']//a/@href").extract()   #获取子分类url
        for i in urls:
            url=i if self.main_url in i else "http://www.gaoxiaogif.com"+i    #处理url格式，补全url
            yield Request(url=url,callback=self.parse)


