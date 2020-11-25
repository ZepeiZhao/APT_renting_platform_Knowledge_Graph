from flask import Flask, render_template, url_for, request,redirect
from models import session,basic_info,parking_allowed,pet_allowed,pet_parking,match_floor_Features,return_res,match_apt_Features,basic,query_list,about_safe,about_transport,about_abstract_airport,about_abstract_park,about_abstract_shop,about_age_apt,about_asian,about_economic,about_education,about_keyList,about_young_people,spacy_keyList,findTitles
from models import *
import json

driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j", "123456"))

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        # data = {}
        county = ""
        try:
            if request.values.get("county_name"):
                county = request.values.get("county_name")
            else:pass
        except:
            county=""
        # data['county'] = county

        pet = ""
        try:
            if request.values.getlist("pet"):
                pet = request.values.get("pet") # [cat,dog]
            else:pass
        except:
            pet = ""

        # return "parking"/""
        parking = ""
        try:
            if request.values.get("parking"):
                parking = True
            else:pass
        except:
            parking = ""


        # return 0 1 2 3 4
        bed = ""
        try:
            if request.values.get("Beds"):
                bed = request.values.get("Beds")
            else:pass
        except:
            bed = ""

        # return 0 1 2 3
        bath = ""
        try:
            if request.values.get("Baths"):
                bath = request.values.get("Baths")
            else:
                pass
        except:
            bath = ""

        sqft = ""
        try:
            if request.values.get("SQFT"):
                sqft = request.values.get("SQFT")
                new_sqft = sqft.split(' ')
                lowest_sqft = new_sqft[0]
                highest_sqft = new_sqft[1]
            else:
                pass
        except:
            sqft = ""
            lowest_sqft = 0
            highest_sqft = 0

        price = ""
        try:
            if request.values.get("price"):
                price = request.values.get("price")
                new_price= price.split(' ')
                lowest_price = new_price[0]
                highest_price = new_price[1]
            else:
                pass
        except:
            price = ""
            highest_price = 0
            lowest_price = 0

        lease = ""
        try:
            if request.values.get("lease_term"):
                lease = request.values.get("lease_term")
            else:
                pass
        except:
            lease = ""


        floor_amenities = []
        try:
            if request.values.getlist("floorplan features"):
                temp_floor = request.values.getlist("floorplan features")
                for i in temp_floor:
                    a = " '" + i + "'"
                    floor_amenities.append(a)
            else:pass
        except:
            floor_amenities = []

        apt_amenities = []
        try:
            if request.values.getlist("apartment features"):
                temp_apt = request.values.getlist("apartment features")
                for i in temp_apt:
                    a = " '" + i + "'"
                    apt_amenities.append(a)
            else:
                pass
        except:
            apt_amenities = []

        keywords = ""
        try:
            if request.values.get("keyword"):
                keywords = request.values.get("keyword")
            else:pass
        except:
            keywords = ""


        if county == "":
            basic_data = session.read_transaction(basic)
        else:
            if pet == "" and parking == "":
                basic_data = session.read_transaction(basic_info,county,lowest_price,highest_price,bed,bath,lowest_sqft,highest_sqft,lease)

            elif pet == "" and parking != "":
                basic_data = session.read_transaction(parking_allowed,county,lowest_price,highest_price,bed,bath,lowest_sqft,highest_sqft,lease,parking)
            elif pet != "" and parking == "":
                basic_data = session.read_transaction(pet_allowed, county, lowest_price, highest_price, bed, bath,lowest_sqft, highest_sqft, lease, pet)
            else:
                basic_data = session.read_transaction(pet_parking, county, lowest_price, highest_price, bed, bath,lowest_sqft, highest_sqft, lease, pet,parking)

        if floor_amenities != []:
            floor_data = session.read_transaction(match_floor_Features,floor_amenities)
        else: floor_data = []
        if apt_amenities != []:
            apt_data = session.read_transaction(match_apt_Features,apt_amenities)
        else: apt_data = []

        if keywords != "":
            query_res = query_list(keywords,1)
        else: query_res = []

        final_list = ['https://www.apartmentfinder.com/California/Bakersfield-Apartments/Springwood-Court-Apartments', 'https://www.apartmentfinder.com/California/Bakersfield-Apartments/Santa-Rosa-Apartments', 'https://www.apartmentfinder.com/California/Bakersfield-Apartments/Liberty-Park-Apartments-yl58m7t', 'https://www.apartmentfinder.com/California/Bakersfield-Apartments/Belcourt-Apartment-Homes-Apartments-6gepmdt', 'https://www.apartmentfinder.com/California/Bakersfield-Apartments/Golden-Valley-Luxury-Apartments']

        intersect_amenities = list(set(apt_data).intersection(set(floor_data)))
        intersect = list(set(query_res).intersection(set(basic_data)).intersection(intersect_amenities))
        intersect1 = list(set(query_res).intersection(set(basic_data)))

        if len(intersect_amenities) > 20:

            if len(intersect) > 20:
                ans3 = intersect
            elif len(intersect1) > 20:
                ans3 = intersect1 + intersect_amenities
            else:
                ans3 = query_res+basic_data+intersect_amenities
        else:
            union_amenities = floor_data+apt_data
            if len(intersect) > 20:
                ans3 = list(set(query_res).intersection(set(basic_data)).intersection(union_amenities))
            elif len(intersect1) > 20:
                ans3 = intersect1 + union_amenities
            else:
                ans3 = query_res+basic_data+union_amenities

        # ans3 = basic_data + floor_data + apt_data + query_res
        ans3 = list(set(ans3))
        # if floor_data!=[] and apt_data!=[]:
        #     ans = basic_data.extend(floor_data)
        #     ans1 = ans.extend(apt_data)
        #     ans2 = ans1.extend(query_res)
        #     ans3 = list(set(ans2))
        # else:
        #     ans = basic_data.extend(query_res)
        #     ans3 = list(set(ans))

        #ans3 = query_res

        f2 = session.read_transaction(return_res,query_res)
        if len(query_res) > 0:
            final_res = f2
        else:
            final_res = session.read_transaction(return_res,ans3)
        length = len(final_res)




        return render_template('resulttest.html',data=final_res,length = length)
        # return redirect(url_for("result"))
        # return apt_data[0]+floor_data[0]
    else:
        return render_template('indextest.html')

@app.route('/result',methods=['POST','GET'])
def result():

    return render_template('resulttest.html')


if __name__ == "__main__":
    app.run(debug=True)

