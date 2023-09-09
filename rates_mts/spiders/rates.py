import scrapy


class RatesSpider(scrapy.Spider):
    name = "rates"
    allowed_domains = ["moskva.mts.ru"]
    start_urls = ["https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile-tv-inet"]

    def parse(self, response):
        pass
