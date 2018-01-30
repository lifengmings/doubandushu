# -*- coding: utf-8 -*-
import scrapy

from douban.items import BookItem


class DoubanbookSpider(scrapy.Spider):
    name = 'doubanbook'
    allowed_domains = ['book.douban.com']

    base_url = 'https://book.douban.com/'
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-all']

    def parse(self, response):
        tag_list = response.xpath('//div/div/table/tbody/tr/td/a/@href').extract()
        for url in tag_list:
            yield response.follow(self.base_url+url, callback=self.parse_tag_detail)

    def parse_tag_detail(self, response):
        item = BookItem()

        for i in response.xpath('//*[@class="subject-item"]'):
            if i:

                item['book_url'] = i.xpath('//li/div/h2/a/@href').extract_first()
                item['name'] = i.xpath('//li/div/h2/a/text()').extract()[0].split()
                item['cover'] = i.xpath('//li/div/a/img/@src').extract_first()

                item['nation'] = i.xpath('normalize-space(//li/div/div/text())').extract()[0].split()[0]
                item['author'] = i.xpath('normalize-space(//li/div/div/text())').extract()[0].split()[1]
                item['translator'] = i.xpath('normalize-space(//li/div/div/text())').extract()[0].split()[3]
                item['press'] = i.xpath('normalize-space(//li/div/div/text())').extract()[0].split()[5]
                item['date_of_press'] = i.xpath('normalize-space(//li/div/div/text())').extract()[0].split()[7]
                item['price'] = i.xpath('normalize-space(//li/div/div/text())').extract()[0].split()[9]

                item['score'] = i.xpath('//li/div/div/span[2]/text()').extract_first()
                item['evaluation_number'] = i.xpath('normalize-space(//li/div/div/span[3]/text())').extract()[0].split()

                item['summary'] = i.xpath('normalize-space(//li/div/p/text())').extract()[0].split()

        yield item

        next_page = response.xpath('//*[@class="paginator"]/span/link/@href').extract()[0]

        if next_page:

            yield scrapy.Request(self.base_url+next_page, callback=self.parse_tag_detail)




