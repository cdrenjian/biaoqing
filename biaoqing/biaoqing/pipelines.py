# -*- coding: utf-8 -*-

from scrapy.utils.misc import md5sum
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class BqPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return image_guid    #保存文件的相对路径+文件名
    def get_media_requests(self, item, info):
            yield Request(item['image_url'][0])   #构造图片下载请求
    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem("Item contains no images")
        item['image_path'] = image_path     #保存图片路径
        return item
