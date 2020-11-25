import jsonlines

writer =  jsonlines.open('allcities_aptFinder.jl', mode='w')

file1 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_bakerfield.jl"
file2 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_fairfield.jl"
file3 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_fresno.jl"
file4 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_los_angeles.jl"
file5 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_modesto.jl"
file6 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_napa.jl"
file7 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_oakland.jl"
file8 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_redwood_city.jl"
file9 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_riverside.jl"
file10 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_sacramento.jl"
file11 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_san_bernardino.jl"
file12 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_san_diego.jl"
file13 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_san_francisco.jl"
file14 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_san_jose.jl"
file15 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_san_rafael.jl"
file16 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_santa_ana.jl"
file17 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_santa_barbara.jl"
file18 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_santa_cruz.jl"
file19 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_santa_rosa.jl"
file20 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_stockton.jl"
file21 = "/Users/pz/Desktop/ds558/pythoncode/project/crawler/c3/c3/spiders/aptFinder_visalia.jl"

with open(file1, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file2, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file3, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file4, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file5, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file6, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file7, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file8, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file9, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)

with open(file10, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file11, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file12, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)

with open(file13, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file14, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file15, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file16, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file17, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file18, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file19, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file20, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)
with open(file21, "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        writer.write(item)