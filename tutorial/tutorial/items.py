import scrapy


class TutorialItem(scrapy.Item):
    # name = scrapy.Field()
    bookTitle = scrapy.Field()
    bookAuthor = scrapy.Field()
    bookTag = scrapy.Field()
