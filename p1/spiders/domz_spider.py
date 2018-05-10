# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 20:57
# @Author  : Mat
# @Email   : mat_wu@163.com
# @File    : domz_spider.py
# @Software: PyCharm
import scrapy


class DomzSpider(scrapy.Spider):
    name = 'domz'
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        fileName = response.url.split('/')[-2] + ".html"
        with open(fileName, "wb") as f:
            f.write(response.body)
