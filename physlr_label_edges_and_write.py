

























from collections import defaultdict
molecule = {}
f = open("/projects/btl/jowong/github/physlr/ground_truth/flchr4.reads.molecule.bed", "r")
h = open("f1chr4_corrected_GT.txt", "w")
for i in f:
    columns= i.split("\t")
    new_mol = columns[3]
    while new_mol in molecule:
        new_mol = new_mol + "_"
    molecule[new_mol] = (int(columns[1]), int(columns[2]))
molecule_keys = list(molecule.keys())
for i in range(len(molecule_keys)):
    molecule_n = molecule_keys[i]
    n = molecule[molecule_n]
    for j in range(i+1, len(molecule_keys)):
        molecule_m = molecule_keys[j]
        m = molecule[molecule_m]
        if (m[0] >= n[0] and m[0]<=n[1]) or (m[1] >= n[0] and m[1]<=n[1]) or (m[1] >= n[1] and m[0]<=n[0]) or (m[1] <= n[1] and m[0]>=n[0]):
            h.write(str(molecule_n).rstrip("_")+"\t"+str(molecule_m).rstrip("_")+"\n")
f.close()
h.close()

# code by Johnathan - start{
from collections import defaultdict
molecule = {}
f = open("/projects/btl/jowong/github/physlr/ground_truth/flchr4.reads.molecule.bed", "r")
#f = open("/projects/btl_scratch/aafshinfard/projects/physlr2/extra/spruce/ws77111.contig2.allreadsbx.molecule.bed", "r")
for i in f:
    columns= i.split("\t")
    molecule[columns[3]] = (int(columns[1]), int(columns[2]))
edges = defaultdict(int)
for i, n in molecule.items():
    for j, m in molecule.items():
        if edges[(j, i)] == 1:
            continue
        if i == j:
            continue
        if (m[0] >= n[0] and m[0]<=n[1]) or (m[1] >= n[0] and m[1]<=n[1]):
            edges[(i,j)] = 1
#}end
fout = "f1chr4_corrected_GT.txt"
fo = open(fout, "w")
for k, v in edges.items():
     if v==1:
         fo.write('\n'+str(k[0]) +'\t'+ str(k[1]) +'\t'+str(v))

fo.close()
