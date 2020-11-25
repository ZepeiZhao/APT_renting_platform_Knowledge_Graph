import csv
import jsonlines
import codecs
import json

#
# result = [json.loads(jline) for jline in jsonl_content.split('\n')]

file = "/Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_la.jl"
res = []
with open(file, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        res.append(item)
print(res[0])



# jsonData = codecs.open(file, 'r', 'utf-8')
csvfile = open('csv_la.csv', 'w', newline='')
writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_ALL)
flag = True
for line in res:
    # dic = json.loads(line)
    if flag:
        # 获取属性列表
        keys = line.keys()
        print (keys)
        writer.writerow(keys) # 将属性列表写入csv中
        flag = False
    # 读取json数据的每一行，将values数据一次一行的写入csv中
    writer.writerow(line.values())
print(dic.values())
# res.close()
csvfile.close()