from scrapy.exceptions import DropItem
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class WikicrawlerPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['title'] == [] or tuple(['title']) in self.ids_seen:
            raise DropItem()
        else:
            self.csvwriter = csv.writer(open('results.csv', 'a'), lineterminator = '\n')
            self.csvwriter.writerow(item['title'])
            self.ids_seen.add(tuple(item['title']))
            return item


    def open_spider(self, spider):
        self.csvwriter = csv.writer(open('results.csv', 'a'))
        self.csvwriter.writerow({'Title', 'ImageURL'})
        self.ids_seen = set()



