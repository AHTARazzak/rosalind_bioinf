'''
Title: Genome Assembly Using Reads
Rosalind ID: GASM
URL: http://rosalind.info/problems/gasm
Goal: A cyclic superstring of minimal length containing every read or its reverse complement.
'''
import sys
from Bio.Seq import Seq

with open(sys.argv[1]) as input_data:
	k_mers = [line.strip() for line in input_data.readlines()]

for kval in range(1,len(k_mers[0])):
	DBG_edge_elmts = set()
	for kmer in k_mers:
		for i in range(kval):
			DBG_edge_elmts.add(kmer[i:len(kmer)+i-kval+1])
			DBG_edge_elmts.add(str(Seq(kmer[i:len(kmer)-kval+i+1]).reverse_complement()))
	k = len(list(DBG_edge_elmts)[0])
	edge = lambda elmt: [elmt[0:k-1],elmt[1:k]]
	DBG_edges = [edge(elmt) for elmt in DBG_edge_elmts]

	cyclics = []
	for repeat in range(2):
		temp_kmer = DBG_edges.pop(0)
		cyclic = temp_kmer[0][-1]
		while temp_kmer[1] in [item[0] for item in DBG_edges]:
			cyclic += temp_kmer[1][-1]
			[index] = [i for i, pair in enumerate(DBG_edges) if pair[0] == temp_kmer[1]]
			temp_kmer = DBG_edges.pop(index)
		cyclics.append(cyclic)

	if len(DBG_edges) == 0:
		break

with open('submit.txt', 'w') as output_file:
	output_file.write(cyclics[0])
#Ali Razzak