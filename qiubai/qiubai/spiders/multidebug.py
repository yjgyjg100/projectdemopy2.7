import scrapy

class DebugSpider(scrapy.Spider):
    name = "debug"
    start_urls = [
        "http://www.qiushibaike.com/article/118115075"
        "http://www.qiushibaike.com/article/118115075"
        "http://www.qiushibaike.com/article/118115797"
    ]

    def parse(self,response):
        from scrapy.shell import inspect_response
        inspect_response(response,self)