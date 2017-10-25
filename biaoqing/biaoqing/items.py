# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class BiaoqingItem(Item):
    image_url=Field()    #图片url
    images=Field()      #图片保存信息
    image_path=Field()  #图片保存路径



