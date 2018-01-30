# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_url = scrapy.Field()
    name = scrapy.Field()
    cover = scrapy.Field()

    nation = scrapy.Field()
    author = scrapy.Field()
    translator = scrapy.Field()
    press = scrapy.Field()
    date_of_press = scrapy.Field()
    price = scrapy.Field()

    score = scrapy.Field()
    evaluation_number = scrapy.Field()

    summary = scrapy.Field()