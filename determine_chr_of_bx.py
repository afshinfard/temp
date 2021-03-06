#!/projects/btl/aafshinfard/virtuEnv/pypy3/bin/pypy3
import argparse
import sys
"""
Amirhossein aafshinfard@bcgsc.ca
"""
def mapBarcodes(barcodict):
    final_dict = dict()
    for key in barcodict.keys():
        final_dict[key] = most_frequent(barcodict[key])
    return final_dict

def most_frequent(List): 
    return max(set(List), key = List.count)
    
def read_read_mapping(files):
    files = ["/dev/stdin" if s == "-" else s for s in files]
    barcodict = dict()
    for file in files:
        with open(file) as fp:
            Lines = fp.readlines() 
            for line in Lines:
                map_tuple = line.split()
                if len(map_tuple)==2:
                    if map_tuple[0] not in barcodict.keys():
                        barcodict[map_tuple[0]] = list()
                    barcodict[map_tuple[0]].append(map_tuple[1])
                else:
                    print(maptuple, file=stderr)
    return barcodict           

def main():
    parser = argparse.ArgumentParser(
        description="Given a file of read barcodes and the chromosome the read maps to, determine for each barcode the main originating chromosome")
    parser.add_argument("files", help="file(s) with two columns, first: barcode of the read and second: the chromosome the read maps to", nargs="+")
    args = parser.parse_args()

    barcodict = read_read_mapping(args.files)
    final_dict = mapBarcodes(barcodict)
    for key in final_dict.keys():
        print(key, final_dict[key], sep="\t")

if __name__ == "__main__":
        main()
