import scrapy


class RatesMtsItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    quota = scrapy.Field()
    options = scrapy.Field()
