# https://www.apartmentfinder.com/California/Los-Angeles-Apartments


import scrapy
from c3.items import C3Item
from scrapy.crawler import CrawlerProcess


class SpiderTry(scrapy.Spider):
    name = 'apartmentFinder'
    allowed_domains = ['apartmentfinder.com']
    # start_urls = ["https://www.apartmentfinder.com/California/Los-Angeles-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Bakersfield-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Fairfield-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Fresno-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Modesto-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Napa-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Oakland-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Redwood-City-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Riverside-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Sacramento-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/San-Bernardino-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/San-Diego-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/San-Francisco-Apartments/Page1"]

    #start_urls = ["https://www.apartmentfinder.com/California/San-Jose-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/San-Rafael-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Santa-Ana-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Santa-Barbara-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Santa-Cruz-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Santa-Rosa-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Stockton-Apartments/Page1"]
    start_urls = ["https://www.apartmentfinder.com/California/Ventura-Apartments/Page1"]
    #start_urls = ["https://www.apartmentfinder.com/California/Visalia-Apartments/Page1"]

    #custom_settings = {'FEED_FORMAT': 'jsonlines', 'FEED_URI': 'aptFinder_bakerfield.jl'}
    custom_settings = {'FEED_FORMAT': 'jsonlines', 'FEED_URI': 'aptFinder_ventura.jl'}
    #custom_settings = {'FEED_FORMAT': 'jsonlines', 'FEED_URI': 'aptFinder_fairfield.jl'}
    #custom_settings = {'FEED_FORMAT': 'jsonlines', 'FEED_URI': 'aptFinder_modesto.jl'}
    #custom_settings = {'FEED_FORMAT': 'jsonlines', 'FEED_URI': 'aptFinder_redwood_city.jl'}
    #custom_settings = {'FEED_FORMAT': 'jsonlines', 'FEED_URI': 'aptFinder_sacramento.jl'}
    #custom_settings = {'FEED_FORMAT': 'jsonlines', 'FEED_URI': 'aptFinder_san_rafael.jl'}
    #custom_settings = {'FEED_FORMAT': 'jsonlines', 'FEED_URI': 'aptFinder_san_bernardino.jl'}
    #custom_settings = {'FEED_FORMAT': 'jsonlines', 'FEED_URI': 'aptFinder_los_angeles.jl'}

    FEED_EXPORT_ENCODING = 'utf-8'
    count = 0
    page_end = 30
    id = 0


    def parse(self, response):

        #nextPage = response.xpath('//div[@class="desc"]/a[@class="lister-page-next next-page"]/@href').extract()

        if self.count < self.page_end:
            self.count += 1
            #next_url = "https://www.apartmentfinder.com/California/Los-Angeles-Apartments/Page"+str(self.count)
            next_url = "https://www.apartmentfinder.com/California/Ventura-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Bakersfield-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Fairfield-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Modesto-Apartments/page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Napa-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Oakland-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Redwood-City-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Riverside-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Sacramento-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/San-Bernardino-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/San-Diego-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/San-Francisco-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/San-Jose-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/San-Rafael-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Santa-Ana-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Santa-Cruz-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Santa-Rosa-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Stockton-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Ventura-Apartments/Page"+str(self.count)
            #next_url = "https://www.apartmentfinder.com/California/Visalia-Apartments/Page"+str(self.count)

            yield scrapy.Request(next_url,callback=self.parse)

        for href in response.xpath('//h2[@class="flex-12 ellipses"]/a/@href').getall():
            yield response.follow(url=href,callback=self.parse_aptFinder)

    def parse_aptFinder(self,response):
        item = C3Item()
        self.id = self.id + 1

        item['id'] = self.id
        item['url'] = response.url

        title = response.xpath('//div[@class="name"]/h1/text()').getall()
        if title: item['title'] = title[0]
        else: item['title'] = ""

        location = response.xpath('//div[@class="address"]/span[@class="mailing-address"]/text()').getall()
        if location: item['location'] = location[0]
        else: item['location'] = ""

        rent_special = [x.strip() for x in response.xpath('//div[@class="specials"]/p[@class="specials-text"]/text()').getall()]
        if rent_special: item['rent_special'] = rent_special[0]
        else: item['rent_special'] = ""

        price_range = response.xpath('//div[@class="price-range"]/text()').getall()
        if price_range: item['price_range'] = price_range[0]
        else: item['price_range'] = ""

        beds = response.xpath('//div[@class="beds"]/text()').getall()
        if beds: item['beds'] = beds[0]
        else: item['beds'] = ""

        bath = response.xpath('//div[@class="baths"]/text()').getall()
        if bath:
            item['bath'] = bath[0]
        else:
            item['bath'] = ""

        lease_term = response.xpath('//section[@id="lease-terms"]/p/text()').getall()
        if lease_term: item['lease_term'] = lease_term[0]
        else: item['lease_term'] = ""

        assigned_garage_parking_price = response.xpath('//span[contains(., "Assigned Garage Parking:")]/../span[@class="right"]/text()').getall()
        if assigned_garage_parking_price: item['assigned_garage_parking_price'] = assigned_garage_parking_price[0]
        else: item['assigned_garage_parking_price'] = ""

        assigned_other_parking_price = response.xpath('//span[contains(., "Assigned Other Parking:")]/../span[@class="right"]/text()').getall()
        if assigned_other_parking_price: item['assigned_other_parking_price'] = assigned_other_parking_price[0]
        else: item['assigned_other_parking_price'] = ""

        cat_rent = response.xpath('//span[contains(., "Cat Rent:")]/../span[@class="right"]/text()').getall()
        if cat_rent: item['cat_rent'] = cat_rent[0]
        else: item['cat_rent'] = ""

        dog_rent = response.xpath('//span[contains(., "Dog Rent:")]/../span[@class="right"]/text()').getall()
        if dog_rent:
            item['dog_rent'] = dog_rent[0]
        else:
            item['dog_rent'] = ""

        application_fee = response.xpath('//span[contains(., "Application Fee:")]/../span[@class="right"]/text()').getall()
        if application_fee:
            item['application_fee'] = application_fee[0]
        else:
            item['application_fee'] = ""

        cat_deposit = response.xpath('//span[contains(., "Cat Deposit:")]/../span[@class="right"]/text()').getall()
        if cat_deposit:
            item['cat_deposit'] = cat_deposit[0]
        else:
            item['cat_deposit'] = ""

        dog_deposit = response.xpath('//span[contains(., "Dog Deposit:")]/../span[@class="right"]/text()').getall()
        if dog_deposit:
            item['dog_deposit'] = dog_deposit[0]
        else:
            item['dog_deposit'] = ""

        apartment_description = response.xpath('//section[@class="xs-12 sm-7 lg-8 description"]/div/p/text()').getall()
        if apartment_description: item['apartment_description'] = apartment_description[0]
        else: item['apartment_description'] = ""

        # office hour
        # Monday
        office_hour_dict = {}
        Mon_time_open = response.xpath('//span[contains(., "Monday")]/../div[@class="hours"]/span[@class="timeOpen"]/text()').getall()
        Mon_time_close = response.xpath('//span[contains(., "Monday")]/../div[@class="hours"]/span[@class="timeClose"]/text()').getall()
        Monday_dict = {}
        if Mon_time_open: Monday_dict['time_open'] = Mon_time_open[0]
        else: Monday_dict['time_open'] = ""
        if Mon_time_close: Monday_dict['time_close'] = Mon_time_close[0]
        else: Monday_dict['time_close'] = ""
        office_hour_dict['Monday'] = Monday_dict

        Tue_time_open = response.xpath('//span[contains(., "Tuesday")]/../div[@class="hours"]/span[@class="timeOpen"]/text()').getall()
        Tue_time_close = response.xpath('//span[contains(., "Tuesday")]/../div[@class="hours"]/span[@class="timeClose"]/text()').getall()
        Tue_dict = {}
        if Tue_time_open:Tue_dict['time_open'] = Tue_time_open[0]
        else: Tue_dict['time_open'] = ""
        if Tue_time_close: Tue_dict['time_close'] = Tue_time_close[0]
        else: Tue_dict['time_close'] = ""
        office_hour_dict['Tuesday'] = Tue_dict

        Wed_time_open = response.xpath('//span[contains(., "Wednesday")]/../div[@class="hours"]/span[@class="timeOpen"]/text()').getall()
        Wed_time_close = response.xpath('//span[contains(., "Wednesday")]/../div[@class="hours"]/span[@class="timeClose"]/text()').getall()
        Wed_dict = {}
        if Wed_time_open: Wed_dict['time_open'] = Wed_time_open[0]
        else: Wed_dict['time_open'] = ""
        if Wed_time_close: Wed_dict['time_close'] = Wed_time_close[0]
        else: Wed_dict['time_close'] = ""
        office_hour_dict['Wednesday'] = Wed_dict

        Thur_time_open = response.xpath('//span[contains(., "Thursday")]/../div[@class="hours"]/span[@class="timeOpen"]/text()').getall()
        Thur_time_close = response.xpath('//span[contains(., "Thursday")]/../div[@class="hours"]/span[@class="timeClose"]/text()').getall()
        Thur_dict = {}
        if Thur_time_open:
            Thur_dict['time_open'] = Thur_time_open[0]
        else:
            Thur_dict['time_open'] = ""
        if Thur_time_close:
            Thur_dict['time_close'] = Thur_time_close[0]
        else:
            Thur_dict['time_close'] = ""
        office_hour_dict['Thursday'] = Thur_dict

        Fri_time_open = response.xpath('//span[contains(., "Friday")]/../div[@class="hours"]/span[@class="timeOpen"]/text()').getall()
        Fri_time_close = response.xpath('//span[contains(., "Friday")]/../div[@class="hours"]/span[@class="timeClose"]/text()').getall()
        Fri_dict = {}
        if Fri_time_open:
            Fri_dict['time_open'] = Fri_time_open[0]
        else:
            Fri_dict['time_open'] = ""
        if Fri_time_close:
            Fri_dict['time_close'] = Fri_time_close[0]
        else:
            Fri_dict['time_close'] = ""
        office_hour_dict['Friday'] = Fri_dict

        Sat_time_open = response.xpath('//span[contains(., "Saturday")]/../div[@class="hours"]/span[@class="timeOpen"]/text()').getall()
        Sat_time_close = response.xpath('//span[contains(., "Saturday")]/../div[@class="hours"]/span[@class="timeClose"]/text()').getall()
        Sat_dict = {}
        if Sat_time_open:
            Sat_dict['time_open'] = Sat_time_open[0]
        else:
            Sat_dict['time_open'] = ""
        if Sat_time_close:
            Sat_dict['time_close'] = Sat_time_close[0]
        else:
            Sat_dict['time_close'] = ""
        office_hour_dict['Saturday'] = Sat_dict

        Sun_time_open = response.xpath('//span[contains(., "Sunday")]/../div[@class="hours"]/span[@class="timeOpen"]/text()').getall()
        Sun_time_close = response.xpath('//span[contains(., "Sunday")]/../div[@class="hours"]/span[@class="timeClose"]/text()').getall()
        Sun_dict = {}
        if Sun_time_open:
            Sun_dict['time_open'] = Sun_time_open[0]
        else:
            Sun_dict['time_open'] = ""
        if Sun_time_close:
            Sun_dict['time_close'] = Sun_time_close[0]
        else:
            Sun_dict['time_close'] = ""
        office_hour_dict['Sunday'] = Sun_dict



        if office_hour_dict: item['office_hour'] = office_hour_dict
        else: item['office_hour'] = {}


        special_features = response.xpath('//section[@id="special-features"]/ul[@class="section-content"]/li/text()').getall()
        if special_features: item['special_features'] = special_features
        else: item['special_features'] = []

        community_features = response.xpath('//section[@id="community-features"]/ul[@class="section-content"]/li/text()').getall()
        if community_features:
            item['community_features'] = community_features
        else:
            item['community_features'] = []

        floorplan_amenities = response.xpath('//section[@id="floorplan-amenities"]/ul[@class="section-content"]/li/text()').getall()
        if floorplan_amenities: item['floorplan_amenities'] = floorplan_amenities
        else: item['floorplan_amenities'] = []

        parking = response.xpath('//section[@id="Parking"]/ul[@class="section-content"]/li/text()').getall()
        if parking:
            item['parking'] = parking
        else:
            item['parking'] = []

        pet_policy = response.xpath('//div[@class="pet-policy"]/div/div/h3[@class="section-subtitle"]/text()').getall()
        if pet_policy:
            item['pet_policy'] = pet_policy[0]
        else:
            item['pet_policy'] = ""

        airport_list = [x.strip() for x in response.xpath('//section[@id="airports"]/div/ul/li/span[@class="name"]/text()').getall()]
        # ['Bob Hope', 'Los Angeles International']
        airport = {}
        if airport_list:
            for name in airport_list:
                airport_dict = {}
                drive_xpath = "//span[contains(., " + "'" + name+ "'" + ")]/../span/span[@class='drive']/span[@class='value']/text()"
                drive = response.xpath(drive_xpath).getall()
                if drive: airport_dict['drive'] = drive[0]
                else: airport_dict['drive'] = ""

                distance_xpath = "//span[contains(., " + "'" + name+ "'" + ")]/../span/span[@class='distance']/span[@class='value']/text()"
                distance = response.xpath(distance_xpath).getall()
                if distance:airport_dict['distance'] = distance[0].strip()
                else: airport_dict['distance'] = ""
                airport[name] = airport_dict
        if airport: item['airport'] = airport
        else: item['airport'] = {}

        # university
        university_list = response.xpath('//section[@id="universities"]/div/ul/li/span[@class="name"]/a/text()').getall()
        universities = {}
        if university_list:
            for u in university_list:
                u_dict = {}
                u = u.replace("'"," ")
                drive_xpath_for_u = "//a[contains(., " + "'" + u + "'" + ")]/../../span[@class='drive-distance']/span[@class='drive']/span[@class='value']/text()"
                drive_for_u = response.xpath(drive_xpath_for_u).getall()
                if drive_for_u: u_dict['drive'] = drive_for_u[0]
                else: u_dict['drive'] = ""

                distance_xpath_for_u = "//a[contains(., " + "'" + u + "'" + ")]/../../span[@class='drive-distance']/span[@class='distance']/span[@class='value']/text()"
                distance_for_u = response.xpath(distance_xpath_for_u).getall()
                if distance_for_u:
                    u_dict['distance'] = distance_for_u[0].strip()
                else:
                    u_dict['distance'] = ""
                universities[u] = u_dict
        if universities: item['universities'] = universities
        else: item['universities'] = ""

        # park and recreation
        park_list = [x.strip() for x in response.xpath('//section[@id="parks-recreation"]/div/ul/li/span[@class="name"]/text()').getall()]
        park_recreation = {}
        if park_list:
            for p in park_list:
                p_dict = {}
                p = p.replace("'"," ")
                drive_xpath_for_p = "//span[contains(., " + "'" + p + "'" + ")]/../span[@class='drive-distance']/span[@class='drive']/span[@class='value']/text()"
                drive_for_p = response.xpath(drive_xpath_for_p).getall()
                if drive_for_p: p_dict['drive'] = drive_for_p[0]
                else: p_dict['drive'] = ""

                distance_xpath_for_p = "//span[contains(., " + "'" + p + "'" + ")]/../span[@class='drive-distance']/span[@class='distance']/span[@class='value']/text()"
                distance_for_p = response.xpath(distance_xpath_for_p).getall()
                if distance_for_p:
                    p_dict['distance'] = distance_for_p[0].strip()
                else:
                    p_dict['distance'] = ""
                park_recreation[p] = p_dict
        if park_recreation: item['park_recreation'] = park_recreation
        else: item['park_recreation'] = ""

        # shopping mall
        shopping_list = response.xpath('//section[@id="malls"]/div/ul/li/span[@class="name"]/a/text()').getall()
        shopping_mall = {}
        if shopping_list:
            for s in shopping_list:
                s_dict = {}
                s = s.replace("'"," ")
                drive_xpath_for_s = "//a[contains(., " + "'" + s + "'" + ")]/../../span[@class='drive-distance']/span[@class='drive']/span[@class='value']/text()"
                drive_for_s = response.xpath(drive_xpath_for_s).getall()
                if drive_for_s:
                    s_dict['drive'] = drive_for_s[0]
                else:
                    s_dict['drive'] = ""

                distance_xpath_for_s = "//a[contains(., " + "'" + s + "'" + ")]/../../span[@class='drive-distance']/span[@class='distance']/span[@class='value']/text()"
                distance_for_s = response.xpath(distance_xpath_for_s).getall()
                if distance_for_u:
                    s_dict['distance'] = distance_for_s[0].strip()
                else:
                    s_dict['distance'] = ""
                shopping_mall[s] = s_dict
        if shopping_mall:
            item['shopping_mall'] = shopping_mall
        else:
            item['shopping_mall'] = ""

        military_list = response.xpath('//section[@id="military-bases"]/div/ul/li/span[@class="name"]/a/text()').getall()
        military = {}
        if military_list:
            for m in military_list:
                m_dict = {}
                m = m.replace("'"," ")
                drive_xpath_for_m = "//a[contains(., " + "'" + m + "'" + ")]/../../span[@class='drive-distance']/span[@class='drive']/span[@class='value']/text()"
                drive_for_m = response.xpath(drive_xpath_for_m).getall()
                if drive_for_m:
                    m_dict['drive'] = drive_for_m[0]
                else:
                    m_dict['drive'] = ""

                distance_xpath_for_m = "//a[contains(., " + "'" + m + "'" + ")]/../../span[@class='drive-distance']/span[@class='distance']/span[@class='value']/text()"
                distance_for_m = response.xpath(distance_xpath_for_m).getall()
                if distance_for_m:
                    m_dict['distance'] = distance_for_m[0].strip()
                else:
                    m_dict['distance'] = ""
                military[m] = m_dict
        if military:
            item['military_bases'] = military
        else:
            item['military_bases'] = ""

        # rating - walk score
        #walk_score = response.xpath('//div[@class="score-description"]/div[@data-value="WalkScore"]/text()').getall()
        # walk_score = response.xpath('//div[@class="score-description"]/div[@data-value="WalkScore"]/text()').getall()
        # #walk_score = response.xpath('//article[@class="neighborhood-rating walk"]/div[@class="layout-row"]/div[@class="score-description"]/div[@class="score"]/text()').getall()
        # if walk_score: item['walk_score'] = walk_score[0]
        # else: item['walk_score'] = ""

        #transit_score = response.xpath('//div[@class="score-description"]/div/div[@class="score-description"]/div[@class="score"]/text()').getall()
        # transit_score = response.xpath('//article[@id="transit"]/div[@class="layout-row"]/div[@class="score-description"]/div[@class="score"]/text()').getall()
        # if transit_score:
        #     item['transit_score'] = transit_score[0]
        # else:
        #     item['transit_score'] = ""
        #
        # bike_score = response.xpath('//section[@id="neighborhood-ratings"]/div/div/article[@class="neighborhood-rating bike"]/div[@class="layout-row"]/div[@class="score-description"]/div[@data-value="TransitScore"]/text()').getall()
        # if bike_score:
        #     item['bike_score'] = bike_score
        # else:
        #     item['bike_score'] = ""

        transit_list = response.xpath('//section[@id="transit-subway"]/div/ul/li/span[@class="name"]/a/text()').getall()
        transit = {}
        if transit_list:
            for t in transit_list:
                t_dict = {}
                t = t.replace("'"," ")
                drive_xpath_for_t = "//a[contains(., " + "'" + t + "'" + ")]/../../span[@class='drive-distance']/span[@class='drive']/span[@class='value']/text()"
                drive_for_t = response.xpath(drive_xpath_for_t).getall()
                if drive_for_t:
                    t_dict['drive'] = drive_for_t[0]
                else:
                    t_dict['drive'] = ""

                distance_xpath_for_t = "//a[contains(., " + "'" + t + "'" + ")]/../../span[@class='drive-distance']/span[@class='distance']/span[@class='value']/text()"
                distance_for_t = response.xpath(distance_xpath_for_t).getall()
                if distance_for_t:
                    t_dict['distance'] = distance_for_t[0].strip()
                else:
                    t_dict['distance'] = ""
                transit[t] = t_dict
        if transit:
            item['transit'] = transit
        else:
            item['transit'] = ""

        commuter_list = response.xpath('//section[@id="commuter-rail"]/div/ul/li/span[@class="name"]/a/text()').getall()
        commuter = {}
        if commuter_list:
            for c in commuter_list:
                c_dict = {}
                c = c.replace("'"," ")
                drive_xpath_for_c = "//a[contains(., " + "'" + c + "'" + ")]/../../span[@class='drive-distance']/span[@class='drive']/span[@class='value']/text()"
                drive_for_c = response.xpath(drive_xpath_for_c).getall()
                if drive_for_c:
                    c_dict['drive'] = drive_for_c[0]
                else:
                    c_dict['drive'] = ""

                distance_xpath_for_c = "//a[contains(., " + "'" + c + "'" + ")]/../../span[@class='drive-distance']/span[@class='distance']/span[@class='value']/text()"
                distance_for_c = response.xpath(distance_xpath_for_c).getall()
                if distance_for_c:
                    c_dict['distance'] = distance_for_c[0].strip()
                else:
                    c_dict['distance'] = ""
                commuter[c] = c_dict
        if commuter:
            item['commuter_rail'] = commuter
        else:
            item['commuter_rail'] = ""


        return item




process = CrawlerProcess()
process.crawl(SpiderTry)
process.start()
