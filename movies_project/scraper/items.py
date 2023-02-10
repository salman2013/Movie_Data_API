# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TorrentcueItem(scrapy.Item):
    heath = scrapy.Field()
    movie_id = scrapy.Field()
    image = scrapy.Field()
    language = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    year = scrapy.Field()


class VofomoviesItem(scrapy.Item):
    movie_id = scrapy.Field()
    image = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    year = scrapy.Field()
