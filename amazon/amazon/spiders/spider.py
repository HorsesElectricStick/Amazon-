# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['amazon.cn']
    start_urls = ['https://www.amazon.cn/s?k=2080ti']

    def parse(self, response):
        for i in response.xpath('//div[@class="s-main-slot s-result-list s-search-results sg-row"]/div/div'):
            url = i.xpath('.//h2/a/@href').get()
            url = response.urljoin(url)
            title = i.xpath('.//h2/a/span/text()').get()
            price = i.xpath('.//span[@class="a-price"]/span/text()').get()
            star = i.xpath('.//i/span/text()').get()
            if star is None:
                star = '无'
            item = AmazonItem(title=title,url=url,price=price,star=star)
            yield item

