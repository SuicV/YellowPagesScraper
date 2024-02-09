# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YellowpagesscraperItem(scrapy.Item):
    """
    Represents an item scraped from Yellow Pages.
    
    Attributes:
        name (scrapy.Field): The name of the business.
        link (scrapy.Field): The URL link to the business.
        phone (scrapy.Field): The phone number of the business.
        address (scrapy.Field): The address of the business.
        website (scrapy.Field): The website of the business.
        rating (scrapy.Field): The rating of the business.
        rating_count (scrapy.Field): The count of ratings for the business.
    """
    name = scrapy.Field()
    link = scrapy.Field()
    phone = scrapy.Field()
    address = scrapy.Field()
    website = scrapy.Field()
    rating = scrapy.Field()
    rating_count = scrapy.Field()
