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
       "http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
    ]

    def parse(self, response):
        fileName = response.url.split('/')[-1] + ".html"
        with open(fileName, "wb") as f:
            f.write(response.body)
        titles = response.xpath("//ul[@class='uk-nav uk-nav-side']//a/text()").extract()
        for title in titles:
            print title
