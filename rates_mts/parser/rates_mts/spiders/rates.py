import re
import json
import scrapy
import html

from rates_mts.items import RatesMtsItem

url = 'https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile-tv-inet'

class RatesSpider(scrapy.Spider):
    name = "rates"
    allowed_domains = ["moskva.mts.ru"]
    start_urls = ["https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile-tv-inet"]

    def parse(self, response):
        a = response.xpath('//script[contains(., "window.globalSettings.tariffs")]').get()
        js_str = re.search('\{[\d,\w,\s,\D]{1,}\}', a)
        array = json.loads(js_str.group(0))
        actual_tarif = array["actualTariffs"]
        for tarif in actual_tarif:
            if tarif['categoryOrder'] == 100:
                try:
                    name = tarif['title']
                    typy = tarif['tariffType']
                    description = html.unescape(tarif['description'])
                    price = 'yt'
                    if tarif['tariffType'] == 'Convergent':
                        price = tarif['convergentTariffSettings']['offer']['totalPrice']['value']
                        quota = tarif['convergentTariffSettings']['offer']['totalPrice']['unit']['display']
                    elif tarif['tariffType']=='HomeServicesTariff':
                        price = tarif['homeTariffSettings']['offer']['totalPrice']['value']
                        quota = tarif['homeTariffSettings']['offer']['totalPrice']['unit']['display']
                    else:
                        price = tarif['subscriptionFee']['numValue']
                        quota = tarif['subscriptionFee']['displayUnit']
                    options = ''
                    for option in tarif['productCharacteristics']:
                        try:
                            options += (' ' + option['value'])
                        except KeyError:
                            continue
                except KeyError:
                    continue
                data = {
                    'name': name,
                    'description': re.sub('<.{,5}>','', description),
                    'price': price,
                    'quota': quota,
                    'options': options,
                    }
                yield RatesMtsItem(data)
