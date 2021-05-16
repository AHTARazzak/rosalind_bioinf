'''
Title: Constructing a De Bruijn Graph
Rosalind ID: DBRU
URL: http://rosalind.info/problems/dbru
Goal: The adjacency list corresponding to the de Bruijn graph corresponding to S∪Src.
'''
from Bio.Seq import Seq
import sys

with open(sys.argv[1]) as input_data:
    k_mers = [line.strip() for line in input_data.readlines()]

DBG_edge_elmts = set()
for kmer in k_mers:
    DBG_edge_elmts.add(kmer)
    DBG_edge_elmts.add(str(Seq(kmer).reverse_complement()))

k = len(k_mers[0])
edge = lambda elmt: '('+elmt[0:k-1]+', '+elmt[1:k]+')'
DBG_edges = [edge(elmt) for elmt in DBG_edge_elmts]

# Write and save the adjacency list.
print('\n'.join(DBG_edges))
with open('submit.txt', 'w') as output_file:
    output_file.write('\n'.join(DBG_edges))

#Ali Razzak

