import pandas as pd
import csv

# remove dplicate
#path = '/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/jlTocsv/sep_data/new_jl_add_county/new_linked_data.csv'
path = '/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/jlTocsv/sep_data/new_jl_add_county/la_new_linked_data.csv'
data = pd.read_csv(path)
data.duplicated()
data.drop_duplicates()


# url1,url2
# url_link_data = data.iloc[:,[0,1]]
# url_link_data.to_csv('./sep_data/sep_csv_table/url_link.csv',index=False)

# aptFinder_location
# location_info_data = data.iloc[:,[0,3,4,-1]]
# location_info_data.to_csv('./sep_data/sep_csv_table/location_info.csv',index=False)

# aptFinder basic info
# aptFinder_basic_info = data.iloc[:,[0,2,5,6,9,16,17,29,30,31,32]]
# aptFinder_basic_info.to_csv('./sep_data/sep_csv_table/aptFinder_basic_info.csv',index=False)

# apts basic info
apts_basic_info = data.iloc[:,[1,8,15,18,19,28]]
apts_basic_info.to_csv('./sep_data/la_apts_basic_info.csv',index=False)