import scrapy


class ES6Spider(scrapy.Spider):
    name = 'ES6'
    allowed_domains = ['es6.ruanyifeng.com']
    start_urls = ['http://es6.ruanyifeng.com']

    def parse(self, response):
        print(response)
