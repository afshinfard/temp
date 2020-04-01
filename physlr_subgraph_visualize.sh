

cat hg004.k40-w32.n100-5000.c2-x.physlr.overlap.m85.mol.tsv | awk '{s+=NF==2}END{print s}' cat hg004.k40-w32.n100-5000.c2-x.physlr.overlap.m85.mol.tsv | awk '{s+=NF==2}END{print s}'

head -n3462510 hg004.k40-w32.n100-5000.c2-x.physlr.overlap.m85.mol.tsv > vertices_hg004.k40-w32.n100-5000.c2-x.physlr.overlap.m85.mol.tsv

grep '_10\s' vertices_hg004.k40-w32.n100-5000.c2-x.physlr.overlap.m85.mol.tsv | wc -l
grep '_10\s' vertices_hg004.k40-w32.n100-5000.c2-x.physlr.overlap.m85.mol.tsv > molecules_10_raw.tsv
cat molecules_10_raw.tsv | awk '{print $1}' > molecules_10_raw2.tsv
mv  molecules_10_raw2.tsv  molecules_10_raw.tsv
cat molecules_10_raw.tsv | sed -e "s/$*_10$//" > molecules_10_barcode.tsv


make hg004.k40-w32.n100-5000.c2-x.physlr.overlap.subgraphs d=10 v="$(paste -d, -s molecules_10_barcode.tsv)"
make hg004.k40-w32.n100-5000.c2-x.physlr.overlap.m85.subgraphs d=10 v="$(paste -d, -s molecules_10_barcode.tsv)"
make hg004.k40-w32.n100-5000.c2-x.physlr.overlap.m85.mol.subgraphs d=10 v="$(paste -d, -s molecules_10_raw.tsv)"

make hg004.k40-w32.n100-5000.c2-x.physlr.overlap.m85.subgraphs/....gv min_component_size=0 -n (use it in the follwing commands)
cd hg004.k40-w32.n100-5000.c2-x.physlr.overlap.m85.subgraphs
for i in *.tsv; do env PYTHONPATH=/projects/btl_scratch/aafshinfard/projects/physlr/publication/jowong/hg004/physlr /projects/btl/aafshinfard/virtuEnv/pypy3/bin/pypy3 /projects/btl_scratch/aafshinfard/projects/physlr/publication/jowong/hg004/physlr/bin/physlr filter --min-component-size=0 -Ogv -V1 $i > "$i.gv"; done
for i in *.tsv.gv; do [[[making eps using command for sfdp.pdf]]]
for i in *.tsv.gv.eps; do convert $i "$i.pdf"



