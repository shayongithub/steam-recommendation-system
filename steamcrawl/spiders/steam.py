import scrapy
import re
import json
from lxml import etree
from steamcrawl.items import SteamcrawlItem
import loguru

class SteamSpider(scrapy.Spider):
    name = 'steam'
    allowed_domains = ['store.steampowered.com/search']
    start_urls = ['https://store.steampowered.com/search/']

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "steamcrawl.middlewares.SteamcrawlMiddleware": 301
        },
        "ITEM_PIPELINES": {
            "steamcrawl.pipelines.SteamcrawlPipeline": 300
        }
    }

    def parse(self, response):

        items = SteamcrawlItem()

        for i in json.loads(response.body):
            data = etree.HTML(i)

            table = data.xpath('//div[@id = "search_resultsRows"]/a/div[@class = "responsive_search_name_combined"]')
            os = []

            for ele in table:
                items['a_name'] = ele.xpath('.//div[@class = "col search_name ellipsis"]/span/text()')[0]
                items['b_date'] = ele.xpath('//div[@class = "col search_released responsive_secondrow"]/text()')[0]
                try:
                    review = \
                    ele.xpath('.//div[@class = "col search_reviewscore responsive_secondrow"]/span/@data-tooltip-html')[
                        0]
                    items['f_n_reviews'] = re.search('[0-9]{3},*[0-9]*,*[0-9]*', review).group()
                    items['g_percent_positive'] = re.search('[0-9]+%+', review).group()
                except:
                    items['f_n_reviews'] = "No review"
                    items['g_percent_positive'] = "No review"

                os_raw = ele.xpath('.//div[@class = "col search_name ellipsis"]/div/span/@class')

                for i in os_raw:
                    os.append(i.replace("platform_img ", ""))

                items['c_os'] = os

                price = ele.xpath('.//div[@class = "col search_price_discount_combined responsive_secondrow"]/div[@class = "col search_price  responsive_secondrow"]/text()')

                if len(price) == 1:#Dont have any account so only have 1 value
                    discount = 0
                    items['d_origin_price'] = price[0].replace("\r\n", "").replace(" ", "").strip()
                else:
                    price = ele.xpath('.//div[@class = "col search_price_discount_combined responsive_secondrow"]/div[@class = "col search_price discounted responsive_secondrow"]/span/strike/text()')[0]
                    discount = ele.xpath('.//div[@class = "col search_price_discount_combined responsive_secondrow"]/div[@class = "col search_discount responsive_secondrow"]/span/text()')[0]
                    items['d_origin_price'] = price.replace("\r\n", "").replace(" ", "").strip()

                items['e_discount'] = discount

                yield items

                os = []
        pass