# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class C3Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    rent_special = scrapy.Field()
    price_range = scrapy.Field()
    beds = scrapy.Field() # 1-3
    bath = scrapy.Field() # 1-3
    lease_term = scrapy.Field()
    assigned_garage_parking_price = scrapy.Field()
    assigned_other_parking_price = scrapy.Field()
    cat_rent = scrapy.Field()
    dog_rent = scrapy.Field()
    application_fee = scrapy.Field()
    cat_deposit = scrapy.Field()
    dog_deposit = scrapy.Field()
    apartment_description = scrapy.Field()
    special_features = scrapy.Field()
    community_features = scrapy.Field()
    floorplan_amenities = scrapy.Field()
    parking = scrapy.Field()
    pet_policy = scrapy.Field()
    office_hour = scrapy.Field()
    airport = scrapy.Field()
    universities = scrapy.Field()
    park_recreation = scrapy.Field()
    shopping_mall = scrapy.Field()
    military_bases = scrapy.Field()
    ratings = scrapy.Field()
    walk_score = scrapy.Field()
    transit_score = scrapy.Field()
    bike_score = scrapy.Field()
    transit = scrapy.Field()
    commuter_rail = scrapy.Field()






