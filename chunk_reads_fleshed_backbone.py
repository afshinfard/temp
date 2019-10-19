import sys
import os
def process(lines=None):
    barcode=lines[0].split(":")[-1]
    #ks = ['barcode', 'name', 'sequence', 'optional', 'quality']
    #return barcode, {k: v for k, v in zip(ks, lines)}
    return barcode, [v for v in lines]

try:
    pfn = sys.argv[1]
    rfn = sys.argv[2]
    ofn = sys.argv[3]
except IndexError as ie:
    raise SystemError("Error: Specify file name\n")

if not os.path.exists(pfn):
    raise SystemError("Error: File does not exist\n")

if not os.path.exists(rfn):
    raise SystemError("Error: File does not exist\n")

# load the read file
n = 4
bx_read_dict = dict()
with open(rfn, 'r') as fh:
    lines = []
    for line in fh:
        lines.append(line.rstrip())
        if len(lines) == n:
            (barcode, record) = process(lines)
            if barcode in bx_read_dict.keys():
                bx_read_dict[barcode].append(record)
            else:
                bx_read_dict[barcode] = record
            lines = []
            #sys.stderr.write("Record: %s\n" % (str(record)))

# load the chunks
chunks_bx = []
chunks_reads = []
with open(pfn, 'r') as fh:
    lines = []
    for line in fh:
        line=line[:-2]
        chunks_bx.append(line.split(" "))
for chunk_bx in chunks_bx:
    chunks_reads.append([read for bx in chunk_bx for read in bx_read_dict[bx]])
iter=0
for chunk_reads in chunks_reads:
    iter+=1
    ofn_t = ofn+"_"+str(iter)+".fq"
    fout = open(ofn_t, "w+")
    for read in chunk_reads:
        for line in read:
            print(line, end = '\n', file=fout)
    fout.close()
