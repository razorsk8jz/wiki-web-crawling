from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from wikiCrawler.items import WikicrawlerItem

class WikispyderSpider(CrawlSpider):
    name = "wikiSpyder"

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 5
    }

    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles']

    rules = (
        Rule(LinkExtractor(canonicalize=True, unique=True), follow=True, callback="parse_link"),
    )

    def parse_link(self, response):
        hxs = HtmlXPathSelector(response)
        item = WikicrawlerItem()
        item['title'] = hxs.select('//h1[contains(@id,"firstHeading")]/text()').extract()
#        item['imgURL'] = hxs.select('//div[contains(@class, "thumbinner")]//a/@href')[0].extract()
        print('---------------------------------------------------------------------')
#        print(item['title'])
#        print(item['imgURL'])
        print(item)
        print('---------------------------------------------------------------------')
        yield item
