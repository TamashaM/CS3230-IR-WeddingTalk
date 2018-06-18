# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeddingTalkSraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    description = scrapy.Field()
    introduction = scrapy.Field()
    url = scrapy.Field()
    overall_rating = scrapy.Field()
    category = scrapy.Field()
    address = scrapy.Field()
    telephone = scrapy.Field()
    website = scrapy.Field()
    email = scrapy.Field()
    map_location = scrapy.Field()
    quality_rating = scrapy.Field()
    timeliness_rating = scrapy.Field()
    reviews = scrapy.Field()





