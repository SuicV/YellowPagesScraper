import scrapy
from urllib.parse import quote

class SearchpagespiderSpider(scrapy.Spider):
    """
    Spider class for scraping search pages on yellowpages.com.
    """

    name = "SearchPageSpider"
    allowed_domains = ["yellowpages.com"]

    def __init__(self, category: str =None, location: str =None, *args, **kwargs):
        super(SearchpagespiderSpider, self).__init__(*args, **kwargs)
        print(category, location)
        self.start_urls = [
            f"https://www.yellowpages.com/search?search_terms={quote(category)}&geo_location_terms={quote(location)}"
        ]
        pass

    def parse(self, response, cur_page=1):
        """
        Parse the response from the search page and extract relevant information.

        Args:
            response: The response object from the search page.
            cur_page: The current page number being parsed.

        Yields:
            A dictionary containing the extracted information for each business listing.
        """

        items = response.css(".scrollable-pane .organic .result")
        for item in items:
            try:
                comments_count = item.css(".rating .count::text").get(0)
                comments_count =  int(comments_count.replace("(", "").replace(")", "")) if comments_count else 0
                
                rating_value = item.css(".rating .result-rating::attr(class)").get(0)
                if rating_value:
                    has_half = True if "half" in rating_value else False
                    rating_value = ["one", "two", "three", "four", "five"].index(rating_value.split(" ")[1])
                    if has_half: rating_value += 0.5

                yield {
                    "name"         : item.css(".business-name span::text").get(),
                    "link"         : "https://www.yellowpages.com" + item.css(".business-name::attr(href)").get(""),
                    "phone"        : item.css(".phones::text").get(),
                    "address"      : item.css(".street-address::text").get("") + item.css(".locality::text").get(""),
                    "website"      : item.css(".track-visit-website::attr(href)").get(),
                    "rating"       : rating_value,
                    "rating_count" : comments_count,
                }
            except Exception as e:
                continue
        next_page = response.css(".pagination .next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse, cb_kwargs={"cur_page": cur_page + 1})
        pass
