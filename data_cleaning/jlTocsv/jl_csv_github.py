# work
import unicodecsv as csv
# import csv
import ujson as json
import gzip
import sys
from tqdm import tqdm


def validate_to_set(x):
    if x is None:
        return set()
    elif isinstance(x, (tuple, list)):
        return set(x)
    elif isinstance(x, str):
        return set([x])
    return -1


def main(in_path, out_path, delim=',', keep_fields=None, skip_fields=None):
    """
    :param str in_path:
    :param str out_path:
    :param str delim:
    :param list|str keep_fields:
    :param list|str skip_fields:
    """
    keep_fields = validate_to_set(keep_fields)
    if keep_fields == -1:
        return
    skip_fields = validate_to_set(skip_fields)
    if skip_fields == -1:
        return

    fmt = in_path.split('.')[-1]
    if fmt == 'gz':
        open_to_use = gzip.open
    else:
        open_to_use = open

    # Read the file once to get a list of all keep fields
    # skip if a set list of keep fields is defined
    line_count = None
    if len(keep_fields) == 0:
        line_count = 0
        for line in tqdm(open_to_use(in_path)):
            keep_fields.update(list(json.loads(line).keys()))
            line_count += 1

        keep_fields.difference_update(skip_fields)

    # force alphabetization
    keep_list = sorted(keep_fields)

    with open(out_path, 'w') as outfile:
        writer = csv.writer(outfile, delimiter=delim)
        writer.writerow(keep_list)
        for line in tqdm(open_to_use(in_path), total=line_count):
            jsn = json.loads(line)
            writer.writerow([jsn[x] if x in jsn else '' for x in keep_list])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python jsonlines2csv.py <in_file> <out_file>]')
        sys.exit(0)
    main(sys.argv[1], sys.argv[2], skip_fields=['content'])

#  python jl_csv_github.py /Users/pz/Desktop/ds558/pythoncode/project/data_cleaning/link_data/link_la.jl csv_la.csv