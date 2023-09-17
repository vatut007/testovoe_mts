import time

import scrapy
from scrapy_playwright.page import PageMethod

from rates_mts.items import RatesMtsItem


class RatesSpider(scrapy.Spider):
    name = "rates"

    def start_requests(self):
        yield scrapy.Request("https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile-tv-inet",
                             meta={"playwright": True,
                                   "playwright_page_methods": [
                                       PageMethod(
                                           'click',
                                           selector='div.tariffs-more-btn'),
                                       ]
                                   })

    def parse(self, response):
        time.sleep(3)
        rates = response.xpath('//mts-tariff-card')
        for rate in rates:
            data = {
                'name': rate.xpath('*//span[@class="card-title__link"]/text()'
                                   ).get(),
                'description': rate.xpath(
                    '''*//div[@class=
                    "card-description card-description__margin"]/text()'''
                    ).get(),
                'price': rate.xpath(
                    '*//div[@class="price-main"]//text()').get(),
                'quota': rate.xpath(
                    '*//div[@class="price-main"]//following-sibling::*/text()'
                    ).get(),
                'options': rate.xpath(
                    '*//li[@class="feature__wrapper"]//text()').getall(),
                }
            yield RatesMtsItem(data)
