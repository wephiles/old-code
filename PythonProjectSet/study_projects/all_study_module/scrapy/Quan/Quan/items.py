# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuanItem(scrapy.Item):
    # define the fields for your item here like:
    image_title = scrapy.Field()
    image_url = scrapy.Field()


class DetailItem(scrapy.Item):
    webpage_url = scrapy.Field()
