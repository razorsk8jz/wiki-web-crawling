from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from wikiCrawler.items import WikicrawlerItem

class WikispyderSpider(CrawlSpider):
    #name of spyder
    name = "wikiSpyder"

    # set initial settings of spider
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'download_delay': 3
    }

    #domains we will allow and where to start
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles']

    #these are the rules the spider will follow as it scrapes
    rules = (
        Rule(LinkExtractor(canonicalize=True, unique=True), follow=True, callback="parse_link"),
    )

    #here we define what we actually want to scrape
    def parse_link(self, response):
        hxs = HtmlXPathSelector(response)
        item = WikicrawlerItem()
#        item['title'] = hxs.select('//h1[contains(@id,"firstHeading")]/text()').extract()
        item['title'] = hxs.select('//title/text()').extract()
        if (hxs.select('(//*[@class="thumbinner"]//img)[1]/@src').extract() == []):
            item['imgURL'] = hxs.select('(//img)[1]/@src').extract()
        else:
            item['imgURL'] = hxs.select('//*[@id="mw-content-text"]/div[4]/div/a/@href').extract()
        print('---------------------------------------------------------------------')
#        print(item['title'])
#        print(item['imgURL'])
        print(item)
        print('---------------------------------------------------------------------')
        yield item
