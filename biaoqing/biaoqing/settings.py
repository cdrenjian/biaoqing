# -*- coding: utf-8 -*-

import os
BOT_NAME = 'biaoqing'

SPIDER_MODULES = ['biaoqing.spiders']
NEWSPIDER_MODULE = 'biaoqing.spiders'

DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {'biaoqing.pipelines.BqPipeline': 1}

project_dir=os.path.abspath(os.path.dirname(__file__))  #获取当前爬虫项目的绝对路径
IMAGES_STORE=os.path.join(project_dir,'image')  #组装新的图片路径


