# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SteamcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    a_name = scrapy.Field()
    b_date = scrapy.Field()
    c_os = scrapy.Field()
    d_origin_price = scrapy.Field()
    e_discount = scrapy.Field()
    f_n_reviews = scrapy.Field()
    g_percent_positive = scrapy.Field()

    pass