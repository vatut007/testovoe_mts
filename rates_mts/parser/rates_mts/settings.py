
BOT_NAME = "rates_mts"

SPIDER_MODULES = ["rates_mts.spiders"]
NEWSPIDER_MODULE = "rates_mts.spiders"
ITEM_PIPELINES = {
   "rates_mts.pipelines.DeleteHaoPipeline": 300,
}
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
FEEDS = {
    'rates_mts/parser/results/rates_mts_%(time)s.csv': {
        'format': 'csv',
        'overwrite': True
    },
    'rates_mts/parser/result_for_web/rates_mts.csv':{
        'format': 'csv',
        'overwrite': True
    }
}
