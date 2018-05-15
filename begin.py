# -*- coding: utf-8 -*-

from scrapy import cmdline
cmdline.execute("scrapy crawl quotes -o douban-book.json".split())
# cmdline.execute("crapy runspider qutoe_spider.py -o quotes.json ".split())