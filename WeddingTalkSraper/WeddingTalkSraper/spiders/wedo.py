import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class WeddingSpider(scrapy.spiders.CrawlSpider):
    name = "wedo"
    start_urls = ['http://www.wedo.lk/']
    allowed_domains = ['wedo.lk']
    rules = [
        Rule(LinkExtractor(allow=("/article","/latest_posts")), callback='parse_link', follow=True)
    ]

    def parse_link(self, response):
        print response.url
        parts = response.url.split("/")
        filename = ""
        if len(parts) >=2:
            filename = 'data/wedo/%s_%s.html' % (parts[-2], parts[-1])
        else:
            filename = 'data/wedo/%s_%s.html' % (parts[0])


        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

