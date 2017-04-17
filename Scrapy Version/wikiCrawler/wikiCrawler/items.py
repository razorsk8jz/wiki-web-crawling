import scrapy

#create variables for the items we want to scrape
class WikicrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    imgURL = scrapy.Field()
    pass
