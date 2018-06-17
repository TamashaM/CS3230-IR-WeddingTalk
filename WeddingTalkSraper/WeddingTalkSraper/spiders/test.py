import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class WeddingSpider(scrapy.spiders.CrawlSpider):
    name = "weddingdirectory"
    start_urls = ['http://www.weddingdirectory.lk/']
    #allowed_domains = ['weddingdirectory.lk']
    rules = [
        Rule(LinkExtractor(allow=("/Category",)), callback='parse_link', follow=True)
    ]

    def parse_link(self, response):
        print response.url
        parts = response.url.split("/")
        filename = ""
        if len(parts) == 2:
            filename = 'data/%s_%s.html' % (parts[-1], 1)
        else:
            filename = 'data/%s_%s.html' % (parts[-2], parts[-1])

        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

