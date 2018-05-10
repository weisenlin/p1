# _*_ coding:utf-8 _*_
import scrapy

class Xiaohuar_Spider(scrapy.spiders.Spider):
        name = "xiaohuar"
        allowed_domains = ["xiaohuar.com"]
        star_urls = [
            "http://www.xiaohuar.com/hua/"
        ]

        def parse(self, response):
            current_url = response.url  #爬虫时请求的url
            body = response.body
            unicode_body = response.body_as_unicode() #返回的html编码