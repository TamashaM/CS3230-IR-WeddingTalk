import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy.loader import ItemLoader

from WeddingTalkSraper.items import WeddingTalkSraperItem


class WeddingSpider(scrapy.spiders.CrawlSpider):
    name = "wedcon"
    start_urls = ['https://www.weddingconnections.lk/']
    allowed_domains = ['weddingconnections.lk']
    rules = [
        Rule(LinkExtractor(), callback='parse_link', follow=True)
    ]

    def parse_link(self, response):
        print response.url
        item = ItemLoader(item=WeddingTalkSraperItem(), response=response)
        item.add_value(field_name='title',
                       value=response.xpath('/html/head/title//text()').extract_first(default='null'))
        item.add_value(field_name='description',
                       value=response.xpath('/html/head/meta[4]/@content').extract_first(default='null'))
        item.add_value(field_name='introduction',
                       value=response.xpath('//*[@id="djcatalog"]/div[5]/div[2]/*/text()').extract())
        item.add_value(field_name='url', value=response.xpath('/html/head/link[1]/@href').extract_first(default='null'))
        item.add_value(field_name='overall_rating',
                       value=response.xpath('//*[@id="djrv-rating-avg-152"]/div/meta[1]/@content').extract_first(
                           default='null'))
        item.add_value(field_name='category',
                       value=response.xpath('//*[@id="kdjcat"]/div/small/a/span/text()').extract_first(default='null'))
        item.add_value(field_name='address',
                       value=response.xpath('//*[@id="kcont"]/div/p[1]/text()').extract_first(default='null'))
        item.add_value(field_name='telephone',
                       value=response.xpath('//*[@id="kcont"]/div/p[2]/span[1]/text()').extract_first(default='null'))
        item.add_value(field_name='website',
                       value=response.xpath('//*[@id="kcont"]/div/p[2]/span[2]/a/text()').extract_first(default='null'))
        item.add_value(field_name='email',
                       value=response.xpath('//*[@id="kcont"]/div/p[2]/span[3]/a/text()').extract_first(default='null'))
        item.add_value(field_name='map_location',
                       value=response.xpath('//*[@id="google_map_box"]/a/@href').extract_first(default='null'))
        item.add_value(field_name='quality_rating', value=response.xpath(
            '//*[@id="djrv-rating-full-152"]/div[1]/div[2]/span[2]/text()').extract_first(default='null'))
        item.add_value(field_name='timeliness_rating', value=response.xpath(
            '//*[@id="djrv-rating-full-152"]/div[2]/div[2]/span[2]/text()').extract_first(default='null'))
        item.add_value(field_name='reviews',
                       value=response.xpath('//*[@id="djrv-reviews-list-148"]/div/div[2]/div[*]/div/p/text()').extract())
        yield item.load_item()


