import scrapy
from scrapy.crawler import CrawlerProcess
import time
import random
import json

class MySpider(scrapy.Spider):
    name = 'apartments'
    def start_requests(self):
        start_url = 'https://www.apartments.com/visalia-ca/{start_page}/'
        for i in range(1,29):
            start_page = i
            yield scrapy.Request(url=start_url.format(start_page=start_page),callback=self.parse_List)

    def parse_List(self, response):
        # get the URL of each apartment
        links = response.xpath('//div[@class="location"]/../a[1]/@href').extract()
        print(len(links))
        for link in links:
            yield response.follow(link, callback=self.parse)

    def parse(self, response):
        # sleep time between request
        time.sleep(random.uniform(0, 0.2))

        apartmentDic = {}
        # url
        apartmentDic['url'] = response.url
        # name
        apartmentDic['name'] = response.xpath('//h1[@class="propertyName"]/text()').extract_first().strip()
        # address
        apartmentDic['address'] = ",".join(response.xpath('//div[@class="propertyAddress"]//span/text()').extract()[:-2])
        # zipcode
        apartmentDic['zipcode'] = response.xpath('//div[@class="propertyAddress"]//span/text()').extract()[-2]
        # choice
        beds = [x.strip() for x in response.xpath('//td[@class="beds"]/span[3]/text()').extract()]
        baths =[x.strip() for x in response.xpath('//td[@class="baths"]/span[3]/text()').extract()]
        rent = [x.strip() for x in response.xpath('//td[@class="rent"]/text()').extract()]
        sqft = [x.strip() for x in response.xpath('//td[@class="sqft"]/text()').extract()]
        available = [x.strip() for x in response.xpath('//td[@class="available"]/text()').extract()]
        apartmentDic['choice'] = list(zip(beds,baths,rent,sqft,available))
        # contact
        apartmentDic['contact'] = response.xpath('//span[@class = "phoneNumber"]/span/text()').extract()
        # parking
        apartmentDic['parking'] = list(zip([x.strip() for x in response.xpath('//div[@class="parkingDetails"]/div/h4/text()').extract()],[x.strip() for x in response.xpath('//div[@class="parkingDetails"]/p/text()').extract()]))
        # property information
        apartmentDic['property information'] = response.xpath('//i[@class="propertyIcon"]/../../ul/li/text()').extract()

        # reviews
        apartmentDic['reviews'] = ''
        try:
            apartmentDic['reviews'] = response.xpath('//p[@class="renterReviewsLabel"]/text()').extract_first().strip()
        except:
            pass
        # ratings
        apartmentDic['rating'] = ''
        try:
            apartmentDic['rating'] = response.xpath('//p[@class="renterReviewsLabel"]/../p[1]/text()').extract_first().strip()
        except:
            pass

        # nearby schools
        school_type = response.xpath('//div[@class="schoolCard"]//p[@class="schoolType"]/text()').extract()
        school_name = response.xpath('//div[@class="schoolCard"]//p[@class="schoolName"]/a/text()').extract()
        school_phone = response.xpath('//div[@class="schoolCard"]//p[@class="schoolPhone"]/text()').extract()
        apartmentDic['nearby schools'] = list(zip(school_name,school_type,school_phone))

        with open('apartments_visalia.jl', mode='a', encoding='utf-8') as f:
                json_record = json.dumps(apartmentDic, ensure_ascii=False)
                f.write(json_record + '\n')

process = CrawlerProcess()
process.crawl(MySpider)
process.start()