# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class C5Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    zipcode = scrapy.Field()
    choice = scrapy.Field()
    contact = scrapy.Field()
    parking = scrapy.Field()
    property_information = scrapy.Field()
    reviews = scrapy.Field()
    rating = scrapy.Field()
    nearby_schools = scrapy.Field()

