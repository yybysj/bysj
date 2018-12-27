# -*- coding: utf-8 -*-

from scrapy import Item,Field

class DoubanItem(Item):
    title = Field()
    movieInfo = Field()
    # star = Field()
    quote = Field()
    