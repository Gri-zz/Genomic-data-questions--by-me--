# 1 : convert FASTA to BED (with biopython) (failed)
"""
from Bio import SeqIO

with open(f1) as in_f, open(f1+'.seq','w') as out_f:
    for record in SeqIO.parse(in_f, 'fasta'):
        out_f.write('{}\t0\t{}\n'.format(record.id, len(record))
"""