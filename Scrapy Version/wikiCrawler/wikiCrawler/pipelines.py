# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class WikicrawlerPipeline(object):
    def __init__(self):
        self.csvwriter = csv.writer(open('results.csv', 'w'))

    def process_item(self, item, spider):
        self.csvwriter.writerow([item['title'][0][0], item['imgURL'][0][1]])
#        self.csvwriter.writerow([item['title'][1], item['imgURL']][1])
        
        return item
