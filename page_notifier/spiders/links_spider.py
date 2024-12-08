import scrapy
import yaml

from scrapy.utils.project import get_project_settings


class LinksSpider(scrapy.Spider):
    start_urls: list
    name: str = "links"
    
    start_urls = ['http://quotes.toscrape.com/page/1/', 'http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        # Follow pagination link
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)