from scrapy.exceptions import DropItem
import csv

class WikicrawlerPipeline(object):
    #initialize ids_seen variable at beginning of program
    def __init__(self):
        self.ids_seen = set()
        
    #choose what items we keep and throw out then write to csv
    def process_item(self, item, spider):
        if item['title'] == [] or tuple(['title']) in self.ids_seen:
            raise DropItem()
        else:
            self.csvwriter = csv.writer(open('results.csv', 'a'), lineterminator = '\n')
            self.csvwriter.writerow(tuple([item['title'], item['imgURL']]))
            self.ids_seen.add(tuple(item['title']))
            return item


    #open csv writer as the spider open and create the header of the csv file
    def open_spider(self, spider):
        self.csvwriter = csv.writer(open('results.csv', 'a'))
        self.csvwriter.writerow({'Title', 'ImageURL'})
        self.ids_seen = set()

    #print closing spider so we know it closed
    def close_spider(self, spider):
        print("closing spider")
