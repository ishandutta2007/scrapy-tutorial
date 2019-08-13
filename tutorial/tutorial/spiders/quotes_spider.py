import scrapy
from ..items import TutorialItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    start_urls = ['http://quotes.toscrape.com/login',]
        
    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()

        return FormRequest.from_response(response,
                                         formdata = {'csfr_token': token,
                                                     'username': 'Test_1',
                                                     'password': 'Testing321'},
                                         callback = self.start_scraping)
        
    def start_scraping(self, response):
        open_in_browser(response)

        items = TutorialItem()

        quotes = response.css('div.quote')

        for quote in quotes:
            titles = quote.css('span.text::text').extract()
            authors = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()

            items['title'] = titles
            items['author'] = authors
            items['tag'] = tags

            yield items
"""
        # Iterating through pages
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
"""