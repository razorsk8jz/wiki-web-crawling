from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class WikispyderSpider(CrawlSpider):
    name = "wikiSpyder"

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 3
    }

    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles']

    rules = (
        Rule(LinkExtractor(canonicalize=True, unique=True), follow=True, callback="parse_link"),
    )

    def parse_link(self, response):
        title = response.xpath('//h1[contains(@id,"firstHeading")]/text()').extract()
        imageURL = response.xpath('//div[contains(@class, "thumbinner")]//a/@href')[0].extract()
        print('---------------------------------------------------------------------')
        print(title)
        print(imageURL)
        print('---------------------------------------------------------------------')
