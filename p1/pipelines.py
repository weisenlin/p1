# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class P1Pipeline(object):
    def __init__(self):
        self.file = codecs.open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        return item


class DoubanBookPipeline(object):
    def process_item(self, item, spider):
        info = item['content'].split(' / ')  # [法] 圣埃克苏佩里 / 马振聘 / 人民文学出版社 / 2003-8 / 22.00元
        item['name'] = item['name']
        item['price'] = info[-1]
        item['edition_year'] = info[-2]
        item['publisher'] = info[-3]
        return item


class TestPipeline(object):
    def __init__(self):
        self.file = codecs.open('douban.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\r\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class DoubanMailPipeline(object):
    def process_item(self, item, spider):
        item['title'] = item['title'].replace(' ', '').replace('\\n', '')
        return item


class DoubanMovieCommentPipeline(object):
    def process_item(self, item, spider):
        return item
