import scrapy

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        retl = response.xpath("//div[@class='tea_con']//h3/text()")
        print(retl)