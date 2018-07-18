# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class WeddingTalkSraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field(output_processor=TakeFirst())
    introduction = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    overall_rating = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field(output_processor=TakeFirst())
    address = scrapy.Field(output_processor=TakeFirst())
    telephone = scrapy.Field(output_processor=TakeFirst())
    website = scrapy.Field(output_processor=TakeFirst())
    email = scrapy.Field(output_processor=TakeFirst())
    map_location = scrapy.Field(output_processor=TakeFirst())
    quality_rating = scrapy.Field(output_processor=TakeFirst())
    timeliness_rating = scrapy.Field(output_processor=TakeFirst())
    reviews = scrapy.Field()





