# Yellow Pages Scraper

A scraper made for the Yellow pages website ([https://www.yellowpages.com](https://www.yellowpages.com)).

## How to use 

to use the the crawler, you should have scrapy installed on your environment:

```
# install scrapy command
$ pip install scrapy
```

to run the spider with the following command

```
$scrapy.exe crawl SearchPageSpider -o output.csv -a category="dentist" -a location="Los Angeles, CA"
```
