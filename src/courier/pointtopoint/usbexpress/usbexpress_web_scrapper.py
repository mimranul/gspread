import scrapy
from scrapy.loader import ItemLoader


class USBExpressWebScrapper(scrapy.Spider):
        name = 'USB Express'
        allowed_domain = ''
        start_urls = []

        def parse(self, response):
            return True
