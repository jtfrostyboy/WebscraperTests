import scrapy


class TierlistspiderSpider(scrapy.Spider):
    name = "tierlistspider"
    allowed_domains = ["u.gg"]
    start_urls = ["https://u.gg/lol/mid-lane-tier-list"]

    def parse(self, response):
        pass
