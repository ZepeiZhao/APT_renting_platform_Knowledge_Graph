import scrapy
from scrapy.crawler import CrawlerProcess
import time
import random
import json
import scrapy
from c5.items import C5Item
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
    name = 'apartments'
    allowed_domains = ['apartments.com']
    start_urls = ['https://www.apartments.com/oakland-ca/15/',]
    custom_settings = {'FEED_FORMAT': 'jsonlines', 'FEED_URI': 'apts_los_angeles.jl'}
    FEED_EXPORT_ENCODING = 'utf-8'
    count = 15
    page_end = 29
    id = 0

    def parse(self, response):
        if self.count < self.page_end:
            self.count += 1
            next_url = "https://www.apartments.com/oakland-ca/"+str(self.count)+"/"
            yield scrapy.Request(next_url, callback=self.parse)
        for href in response.xpath('//div[@class="location"]/../a/@href').getall():
            yield response.follow(url=href,callback=self.parse_apts)


    def parse_apts(selfself,response):
        item = C5Item()
        item['url'] = response.url
        name = response.xpath('//h1[@class="propertyName"]/text()').getall()
        if name:
            item['name'] = name[0].strip()
        else:
            item['name'] = ""
        return item


    # def parse(self, response):
    #     # sleep time between request
    #     time.sleep(random.uniform(0, 0.2))
    #
    #     apartmentDic = {}
    #     # url
    #     apartmentDic['url'] = response.url
    #     # name
    #     apartmentDic['name'] = response.xpath('//h1[@class="propertyName"]/text()').extract_first().strip()
    #     # address
    #     apartmentDic['address'] = ",".join(response.xpath('//div[@class="propertyAddress"]//span/text()').extract()[:-2])
    #     # zipcode
    #     apartmentDic['zipcode'] = response.xpath('//div[@class="propertyAddress"]//span/text()').extract()[-2]
    #     # choice
    #     beds = [x.strip() for x in response.xpath('//td[@class="beds"]/span[3]/text()').extract()]
    #     baths =[x.strip() for x in response.xpath('//td[@class="baths"]/span[3]/text()').extract()]
    #     rent = [x.strip() for x in response.xpath('//td[@class="rent"]/text()').extract()]
    #     sqft = [x.strip() for x in response.xpath('//td[@class="sqft"]/text()').extract()]
    #     available = [x.strip() for x in response.xpath('//td[@class="available"]/text()').extract()]
    #     apartmentDic['choice'] = list(zip(beds,baths,rent,sqft,available))
    #     # contact
    #     apartmentDic['contact'] = response.xpath('//span[@class = "phoneNumber"]/span/text()').extract()
    #     # parking
    #     apartmentDic['parking'] = list(zip([x.strip() for x in response.xpath('//div[@class="parkingDetails"]/div/h4/text()').extract()],[x.strip() for x in response.xpath('//div[@class="parkingDetails"]/p/text()').extract()]))
    #     # property information
    #     apartmentDic['property information'] = response.xpath('//i[@class="propertyIcon"]/../../ul/li/text()').extract()
    #
    #     # reviews
    #     apartmentDic['reviews'] = ''
    #     try:
    #         apartmentDic['reviews'] = response.xpath('//p[@class="renterReviewsLabel"]/text()').extract_first().strip()
    #     except:
    #         pass
    #     # ratings
    #     apartmentDic['rating'] = ''
    #     try:
    #         apartmentDic['rating'] = response.xpath('//p[@class="renterReviewsLabel"]/../p[1]/text()').extract_first().strip()
    #     except:
    #         pass
    #
    #     # nearby schools
    #     school_type = response.xpath('//div[@class="schoolCard"]//p[@class="schoolType"]/text()').extract()
    #     school_name = response.xpath('//div[@class="schoolCard"]//p[@class="schoolName"]/a/text()').extract()
    #     school_phone = response.xpath('//div[@class="schoolCard"]//p[@class="schoolPhone"]/text()').extract()
    #     apartmentDic['nearby schools'] = list(zip(school_name,school_type,school_phone))
    #
    #     with open('./apartment_data/apartments_los-angeles.jl', mode='a', encoding='utf-8') as f:
    #             json_record = json.dumps(apartmentDic, ensure_ascii=False)
    #             f.write(json_record + '\n')

process = CrawlerProcess()
process.crawl(MySpider)
process.start()