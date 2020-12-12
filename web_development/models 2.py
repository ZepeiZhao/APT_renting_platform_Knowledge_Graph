from neo4j import GraphDatabase
import en_core_web_md
from spacy.matcher import Matcher


driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j", "123456"))


def basic(tx):
    res = [] # url list
    query = "MATCH (p:aptFinder)-[:LINKS]->(q:apts)-[:HAS_FLOORPLAN]->(f:floorplan) RETURN DISTINCT p.aptFinder_url LIMIT 50"
    for record in tx.run(
       query
    ):
        res.append(record["p.aptFinder_url"])
    return res

def basic_info(tx,county,lowest_price,highest_price,bed,bath,lowest_sqft,highest_sqft,lease):
    res = [] # url list
    query = "MATCH (p:aptFinder)-[:LINKS]->(q:apts)-[:HAS_FLOORPLAN]->(f:floorplan) WHERE p.county = " + '"' \
            + str(county) + '"' + " and p.lowest_price >= " + str(lowest_price) + " and p.highest_price <= " \
            + str(highest_price) + " and f.bed >= " + str(bed) + " and f.bath >= " + str(bath) + " and f.sqft >= " \
            + str(lowest_sqft) + " and f.sqft <= " + str(highest_sqft) + " and p.shortest_lease_term <= " \
            + str(lease) + " RETURN DISTINCT p.aptFinder_url LIMIT 10"
    for record in tx.run(
       query,county = county,lowest_sqft=lowest_sqft,lowest_price=lowest_price,bath=bath,
        bed=bed,highest_sqft=highest_sqft,highest_price=highest_price,lease=lease
    ):
        res.append(record["p.aptFinder_url"])
    return res

def parking_allowed(tx,county,lowest_price,highest_price,bed,bath,lowest_sqft,highest_sqft,lease,parking):
    res = []
    query = "MATCH (p:aptFinder)-[:LINKS]->(q:apts)-[:HAS_FLOORPLAN]->(f:floorplan) WHERE p.county = " \
            + '"' + str(county) + '"' + " and p.lowest_price >= " + str(lowest_price) + " and p.highest_price <= " \
            + str(highest_price) + " and f.bed >= " + str(bed) + " and f.bath >= " + str(bath) + " and f.sqft >= " \
            + str(lowest_sqft) + " and f.sqft <= " + str(highest_sqft) + " and p.shortest_lease_term <= " + str(lease) \
            + " and q.parking = True RETURN DISTINCT p.aptFinder_url LIMIT 10"
    for record in tx.run(
       query,county = county,lowest_sqft=lowest_sqft,lowest_price=lowest_price,bath=bath,
        bed=bed,highest_sqft=highest_sqft,highest_price=highest_price,lease=lease,parking=parking
    ):
        res.append(record["p.aptFinder_url"])
    return res

def pet_allowed(tx,county,lowest_price,highest_price,bed,bath,lowest_sqft,highest_sqft,lease,pet):
    res = []
    query = "MATCH (p:aptFinder)-[:LINKS]->(q:apts)-[:HAS_FLOORPLAN]->(f:floorplan) WHERE p.county = " + '"' + str(
        county) + '"' + " and p.lowest_price >= " + str(lowest_price) + " and p.highest_price <= " + str(
        highest_price) + " and f.bed >= " + str(bed) + " and f.bath >= " + str(bath) + " and f.sqft >= " + str(
        lowest_sqft) + " and f.sqft <= " + str(highest_sqft) + " and p.shortest_lease_term <= " + str(
        lease) + " and p.cat_policy = True or p.dog_policy = True RETURN DISTINCT p.aptFinder_url LIMIT 10"
    for record in tx.run(
            query, county=county, lowest_sqft=lowest_sqft, lowest_price=lowest_price, bath=bath,
            bed=bed, highest_sqft=highest_sqft, highest_price=highest_price, lease=lease, pet=pet
    ):
        res.append(record["p.aptFinder_url"])
    return res

def pet_parking(tx,county,lowest_price,highest_price,bed,bath,lowest_sqft,highest_sqft,lease,pet,parking):
    res = []
    res_info = []
    query = "MATCH (p:aptFinder)-[:LINKS]->(q:apts)-[:HAS_FLOORPLAN]->(f:floorplan) WHERE p.county = " + '"' + str(
        county) + '"' + " and p.lowest_price >= " + str(lowest_price) + " and p.highest_price <= " + str(
        highest_price) + " and f.bed >= " + str(bed) + " and f.bath >= " + str(bath) + " and f.sqft >= " + str(
        lowest_sqft) + " and f.sqft <= " + str(highest_sqft) + " and p.shortest_lease_term <= " + str(
        lease) + " and (p.cat_policy = True or p.dog_policy = True) and q.parking = True RETURN DISTINCT p.aptFinder_url, p.title LIMIT 10"
    for record in tx.run(
            query, county=county, lowest_sqft=lowest_sqft, lowest_price=lowest_price, bath=bath,
            bed=bed, highest_sqft=highest_sqft, highest_price=highest_price, lease=lease, pet=pet,parking=parking
    ):
        temp = {}
        temp['aptFinder_url'] = record["p.aptFinder_url"]
        temp['title'] = record["p.title"]
        res_info.append(temp)
        res.append(record["p.aptFinder_url"])
        # res = list(set(res))
    return res

def match_floor_Features(tx,floor_amenities):
    res = []
    res_info = []
    for record in tx.run("MATCH (n:aptFinder) WITH split(substring(n.foolorplan_amenities, 1, size(n.foolorplan_amenities)-2),',')"
                         "as numList,$floor_amenities as b, n as c WHERE size(apoc.coll.intersection(numList,b))=size(b) "
                         "MATCH(c:aptFinder)-[r:LINKS]->(k:apts) RETURN c.aptFinder_url,k.apts_url ORDER BY k.rating LIMIT 10",
                         floor_amenities = floor_amenities):
        temp = {}
        temp['aptFinder_url'] = record["c.aptFinder_url"]
        temp['apts_url'] = record["k.apts_url"]
        res_info.append(temp)
        res.append(record["c.aptFinder_url"])
    if len(res) == 0:
        for record in tx.run("MATCH (n:aptFinder) WITH split(substring(n.foolorplan_amenities, 1, size(n.foolorplan_amenities)-2),',')"
                             "as numList, $floor_amenities as b,n as c WHERE any(x IN numList WHERE x IN b) "
                             "MATCH(c:aptFinder)-[r:LINKS]->(k:apts) RETURN c.aptFinder_url,k.apts_url ORDER BY k.rating LIMIT 10",
                             floor_amenities = floor_amenities):
            temp = {}
            temp['aptFinder_url'] = record["c.aptFinder_url"]
            temp['apts_url'] = record["k.apts_url"]
            res_info.append(temp)
            res.append(record["c.aptFinder_url"])
    # res = list(set(res))
    return res


templist = [" 'Elevator'"," 'Storage Space'"," 'Fitness Center'"," 'Grill'"]
def match_apt_Features(tx,apt_amenities):
    res = []
    res_info = []
    for record in tx.run("MATCH (n:aptFinder) WITH split(substring(n.community_features, 1, size(n.community_features)-2),',')"
                         "as numList,$apt_amenities as b, n as c WHERE size(apoc.coll.intersection(numList,b))=size(b) "
                         "MATCH(c:aptFinder)-[r:LINKS]->(k:apts) RETURN c.aptFinder_url,k.apts_url ORDER BY k.rating LIMIT 10",
                         apt_amenities = apt_amenities):
        temp = {}
        temp['aptFinder_url'] = record["c.aptFinder_url"]
        temp['apts_url'] = record["k.apts_url"]
        res_info.append(temp)
        res.append(record["c.aptFinder_url"])
    if len(res) == 0:
        for record in tx.run("MATCH (n:aptFinder) WITH split(substring(n.community_features, 1, size(n.community_features)-2),',')"
                             "as numList, $apt_amenities as b,n as c WHERE any(x IN numList WHERE x IN b) MATCH(c:aptFinder)-[r:LINKS]->(k:apts) "
                             "RETURN c.aptFinder_url,k.apts_url ORDER BY k.rating LIMIT 10",apt_amenities = apt_amenities):
            temp = {}
            temp['aptFinder_url'] = record["c.aptFinder_url"]
            temp['apts_url'] = record["k.apts_url"]
            res_info.append(temp)
            res.append(record["c.aptFinder_url"])
    # res = list(set(res))
    return res

res_url_list = ['https://www.apartmentfinder.com/California/Bakersfield-Apartments/Springwood-Court-Apartments', 'https://www.apartmentfinder.com/California/Bakersfield-Apartments/Santa-Rosa-Apartments', 'https://www.apartmentfinder.com/California/Bakersfield-Apartments/Liberty-Park-Apartments-yl58m7t', 'https://www.apartmentfinder.com/California/Bakersfield-Apartments/Belcourt-Apartment-Homes-Apartments-6gepmdt', 'https://www.apartmentfinder.com/California/Bakersfield-Apartments/Golden-Valley-Luxury-Apartments']

def return_res(tx,res_url_list):
    res = []
    # for i in range(len(res_url_list)):
    query = "MATCH (a:aptFinder)-[:LOCATES_IN]->(l:locationInfo) MATCH(a:aptFinder)-[:LINKS]->(a2:apts) " \
            "WHERE a.aptFinder_url in $res_url_list RETURN DISTINCT a.title, a.aptFinder_url, a.description,a2.apts_url,l.zipcode, " \
            "l.covid_confirmed_cases,a.location,l.covid_deaths,a.lowest_price,a2.phone,a2.rating," \
            "a2.reviews,a.rent_special,a.cat_policy,a.dog_policy,a.foolorplan_amenities,a.community_features," \
            "a.office_hour,l.bachelorplus,a2.parking,a.shortest_lease_term,l.employ,l.hh_ratio_married ," \
            "l.jail,l.meanic_fam,l.mid_age,l.popu_ratio_asian,l.popu_ratio_black,l.popu_ratio_white ORDER BY a2.rating DESC LIMIT 50"
    #query = "MATCH (n:aptFinder) WHERE n.aptFinder_url = " + '"'+ res_url_list[i] + '"'+" RETURN n.title"
    for record in tx.run(query,res_url_list=res_url_list):
        temp = {}
        temp['title'] = record["a.title"].title()
        temp['aptFinder_url'] = record["a.aptFinder_url"]
        temp['address'] = record["a.location"]
        temp['apts_url'] = record["a2.apts_url"]
        temp['cat_policy'] = record["a.cat_policy"]
        temp['dog_policy'] = record["a.dog_policy"]
        temp['description'] = record["a.description"]
        temp['office_hour'] = record["a.office_hour"]
        temp['shortest_lease_term'] = record["a.shortest_lease_term"]
        temp['rent_special'] = record["a.rent_special"]
        temp['lowest_price'] = record["a.lowest_price"]
        temp['floorplan_amenities'] = record["a.foolorplan_amenities"].strip('"').replace("['",'').replace("']",'').replace(" '","").split("',")
        temp['community_features'] = record["a.community_features"].strip('"').replace("['",'').replace("']",'').replace(" '","").split("',")
        temp['phone'] = record["a2.phone"]
        temp['rating'] = record["a2.rating"]
        temp['reviews'] = record["a2.reviews"]
        temp['parking'] = record["a2.parking"]
        temp['white_ratio'] = record["l.popu_ratio_white"]
        temp['black_ratio'] = record["l.popu_ratio_black"]
        temp['asian_ratio'] = record["l.popu_ratio_asian"]
        temp['meanic_fam'] = record["l.meanic_fam"]
        temp['jail'] = record["l.jail"]
        temp['employ'] = record["l.employ"]
        temp['marriage'] = record["l.hh_ratio_married"]
        temp['bachelorplus'] = record["l.bachelorplus"]
        temp['covid_confirmed'] = record["l.covid_confirmed_cases"]
        temp['covid_deaths'] = record["l.covid_deaths"]
        temp['zipcode'] = record["l.zipcode"]


        res.append(temp)
    return res

def about_safe(tx):
    res = []
    for record in tx.run("MATCH(n:aptFinder)-[r1:LINKS]->(m:apts) MATCH(n:aptFinder)-[r2:LOCATES_IN]->(lo:locationInfo) WHERE lo.covid_confirmed_cases<315616 and lo.covid_deaths<7141 and lo.jail<=0.01 return n.aptFinder_url ORDER BY -m.rating"):
        res.append(record["n.aptFinder_url"])
    return res

def about_transport(tx):
    res = []
    for record in tx.run("MATCH(n:aptFinder)-[r:NEARBY_TRANSIT]->(t:transits) WITH n, count(DISTINCT t)as numK WHERE numK>=3 RETURN n.aptFinder_url order by -numK"):
        res.append(record["n.aptFinder_url"])
    return res

def about_abstract_shop(tx):
    res = []
    for record in tx.run("MATCH(n:aptFinder)-[r:NEARBY_SHOPPING_MALL]->(cc) WITH n, count(DISTINCT cc)as numK WHERE numK>=3 RETURN n.aptFinder_url,numK LIMIT 50"):
        res.append(record["n.aptFinder_url"])
    return res

def about_abstract_airport(tx):
    res = []
    for record in tx.run("MATCH(n:aptFinder)-[r:NEARBY_AIRPORT]->(cc) WITH n, count(DISTINCT cc)as numK WHERE numK>=3 RETURN n.aptFinder_url,numK LIMIT 50"):
        res.append(record["n.aptFinder_url"])
    return res

def about_abstract_park(tx):
    res = []
    for record in tx.run("MATCH(n:aptFinder)-[r:NEARBY_PARK]->(cc) WITH n, count(DISTINCT cc)as numK WHERE numK>=3 RETURN n.aptFinder_url,numK LIMIT 50"):
        res.append(record["n.aptFinder_url"])
    return res


def about_age_apt(tx):
    res = []
    for record in tx.run("MATCH(n:aptFinder)-[r:LINKS]->(m:apts) WHERE m.built_in_time>2010 RETURN n.aptFinder_url LIMIT 50 ORDER BY -m.built_in_time"):
        res.append(record["n.aptFinder_url"])
    return res

def about_economic(tx):
    res = []
    for record in tx.run("MATCH(n:aptFinder)-[r:LOCATES_IN]->(ll) WHERE ll.employ>0.725 and ll.meanic_fam > 91644.0 RETURN n.aptFinder_url,ll.employ,ll.meanic_fam ORDER BY -ll.employ*ll.meanic_fam"):
        res.append(record["n.aptFinder_url"])
    return res

def about_asian(tx):
    res = []
    for record in tx.run("MATCH(n:aptFinder)-[r:LOCATES_IN]->(ll) WHERE ll.popu_ratio_asian>0.105 RETURN n.aptFinder_url,ll.popu_ratio_asian ORDER BY -ll.popu_ratio_asian"):
        res.append(record["n.aptFinder_url"])
    return res

def about_young_people(tx):
    res = []
    for record in tx.run("MATCH(n:aptFinder)-[r:LOCATES_IN]->(ll) WHERE ll.mid_age<38.075 and ll.hh_ratio_married < 0.48 RETURN n.aptFinder_url,ll.mid_age,ll.hh_ratio_married ORDER BY ll.mid_age"):
        res.append(record["n.aptFinder_url"])
    return res

def about_education(tx):
    res = []
    for record in tx.run("MATCH(n:aptFinder)-[r1:NEARBY_UNIVERSITY]->(uu) MATCH(n:aptFinder)-[r2:LOCATES_IN]->(ll) WITH n, ll, count(DISTINCT uu)as numK WHERE numK>=3 and  ll.bachelorplus>0.32 and ll.highschool > 0.84 RETURN n.aptFinder_url,ll.bachelorplus,ll.highschool LIMIT 50 ORDER BY -ll.highschool, -ll.bachelorplus, -numK"):
        res.append(record["n.aptFinder_url"])
    return res

def findTitles(text):
    filtered = " ".join([x if x.istitle() else " " for x in text.split()])
    return [y.strip() for y in filtered.split("  ") if y]

def about_keyList(tx,newList):
    res = []
    # Capital related - spots
    for record in tx.run("MATCH(n:aptFinder)-[r1:NEARBY_UNIVERSITY]->(uu) MATCH(n:aptFinder)-[r2:NEARBY_TRANSIT]->(tt) MATCH(n:aptFinder)-[r3:NEARBY_SHOPPING_MALL]->(ss) MATCH(n:aptFinder)-[r4:NEARBY_PARK]->(pp) MATCH(n:aptFinder)-[r5:NEARBY_AIRPORT]->(aa) WITH $newList as numList,n,uu,tt,ss,pp,aa WHERE any(x IN numList WHERE x=uu.university or x=tt.transit or x=ss.shopping_mall or x=pp.park or x=aa.airport) RETURN DISTINCT n.aptFinder_url LIMIT 50",newList = newList):
        res.append(record["n.aptFinder_url"])
    # Capital related - address
    for record in tx.run("MATCH(n:aptFinder) WITH $newList as numList,n WHERE any(x IN numList WHERE x= n.location) RETURN DISTINCT n.aptFinder_url LIMIT 50",newList = newList):
        res.append(record["n.aptFinder_url"])
    # # Capital related - celebrity
    # for record in tx.run("MATCH(n:aptFinder)-[r1:LOCATES_IN]->(ll)<-[]-(p1:celebrity) MATCH(n:aptFinder)-[r2:NEARBY_UNIVERSITY]->(uu)<-[]-(p2:celebrity) WITH $newList as personlist,n,p1,p2 WHERE any(x IN personlist WHERE x=p1.name or x=p2.name) RETURN DISTINCT n.aptFinder_url LIMIT 50",newList = newList):
    #     res.append(record["n.aptFinder_url"])
    return res

def spacy_keyList(q):
    nlp = en_core_web_md.load()
    doc = nlp(q)
    # for w in doc:
    #     print(f'{w.text:15s}[{w.tag_:5s}|{w.lemma_:20s}|{w.pos_:6s}]')
    # for ent in doc.ents:
    #     print(f'{ent.text:15s}[{ent.label_}]')

    pattern1 = [{'ENT_TYPE': 'ORG', "OP": "+"}]
    pattern2 = [{'ENT_TYPE': 'PERSON', "OP": "+"}]
    pattern3 = [{'ENT_TYPE': 'FAC', "OP": "+"}]
    pattern4 = [{'ENT_TYPE': 'LOC', "OP": "+"}]
    pattern5 = [{'ENT_TYPE': 'GPE', "OP": "+"}]
    pattern6 = [{'ENT_TYPE': 'CARDINAL', "OP": "*"}, {'ENT_TYPE': 'LOC', "OP": "+"}, {"IS_PUNCT": True},
                {'ENT_TYPE': 'GPE', "OP": "+"}, {"IS_PUNCT": True}, {'ENT_TYPE': 'GPE', "OP": "+"}]
    pattern7 = [{'ENT_TYPE': 'FAC', "OP": "+"}, {"IS_LOWER": True}, {'ENT_TYPE': 'CARDINAL', "OP": "?"},
                {'ENT_TYPE': 'GPE', "OP": "+"}]
    matcher = Matcher(nlp.vocab)
    matcher.add("name1", None, pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7)
    matches = matcher(doc)
    keyList = []
    for m_id, s, e in matches:
        keyword = doc[s:e].text
        if len(keyword) > 1 and len(doc[s:e].text.split()) > 1:
            keyList.append(keyword)
    return keyList


def query_list(q,choose_method):
    # get a query
    # q = "apartment near 6201 Hollywood Blvd and Gloria Molina or Kathleen Sky"
    # choose_method = 1
    q2 = q.lower()
    # Use key words
    # about safety
    check_safe = False
    safe_list = ["safe","secure","security","crime","jail","covid"]
    for i in safe_list:
        if i in q2:
            check_safe = True
            break
    # about transport
    check_transport = False
    transport_list = ["transport","traffic","convenient","light","little","busy","transit"]
    for i in transport_list:
        if i in q2:
            check_transport = True
            break
    # about abstract shop
    check_abstract_shop = False
    abstract_shop_list = ["center","market","shop","buy","mall"]
    for i in abstract_shop_list:
        if i in q2:
            check_abstract_shop = True
            break
    # about abstract airport
    check_abstract_airport = False
    abstract_airport_list = ["airport","airfield"]
    for i in abstract_airport_list:
        if i in q2:
            check_abstract_airport = True
            break
    # about abstract park
    check_abstract_park = False
    abstract_park_list = ["park", "museum","spot","aquarium","garden","beach","lake","canyon","observatory","reserve","arboretum","science"]
    for i in abstract_park_list:
        if i in q2:
            check_abstract_park = True
            break
    # about age of apt
    check_apt_age = False
    apt_age_list = ["new","built","old","age"]
    for i in apt_age_list:
        if i in q2:
            check_apt_age = True
            break
    # about economic
    check_economic = False
    economic_list = ["job","income","economic","financial","economy"]
    for i in economic_list:
        if i in q2:
            check_economic = True
            break
    # about race
    check_asian = False
    asian_list = ["asian"]
    for i in asian_list:
        if i in q2:
            check_asian = True
            break
    # about young people
    check_young_people = False
    young_people_list = ["young","single","friend","vibrant"]
    for i in young_people_list:
        if i in q2:
            check_young_people = True
            break
    # about education
    check_education = False
    education_list = ["education","educated","college","institution","school","university","universities"]
    for i in education_list:
        if i in q2:
            check_education = True
            break
    # about Capital related
    if choose_method == 1:
        keyList = findTitles(q)
    elif choose_method == 2:
        keyList = spacy_keyList(q)

    # driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "123456"))
    # session = driver.session()
    result = []
    if len(keyList):
        result.extend(session.read_transaction(about_keyList,keyList))
    #     print(keyList)
    if len(result) <= 3:
        if check_safe:
            result.extend(session.read_transaction(about_safe))
        if check_transport:
            result.extend(session.read_transaction(about_transport))
        if check_abstract_shop:
            result.extend(session.read_transaction(about_abstract_shop))
        if check_abstract_airport:
            result.extend(session.read_transaction(about_abstract_airport))
        if check_abstract_park:
            result.extend(session.read_transaction(about_abstract_park))
        if check_apt_age:
            result.extend(session.read_transaction(about_age_apt))
        if check_economic:
            result.extend(session.read_transaction(about_economic))
        if check_asian:
            result.extend(session.read_transaction(about_asian))
        if check_young_people:
            result.extend(session.read_transaction(about_young_people))
        if check_education:
            result.extend(session.read_transaction(about_education))

    final_result = list(set(result))
    return final_result


session=driver.session()

