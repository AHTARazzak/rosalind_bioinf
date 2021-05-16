'''
Title: Genome Assembly with Perfect Coverage
Rosalind ID: PCOV
URL: http://rosalind.info/problems/pcov
Goal: A cyclic superstring of minimal length containing the reads (thus corresponding to a candidate cyclic chromosome).
'''
import sys

with open(sys.argv[1]) as input_data:
	k_mers = [line.strip() for line in input_data.readlines()]

DBG_edge_elmts = set()
for kmer in k_mers:
	DBG_edge_elmts.add(kmer)

k = len(k_mers[0])
edge = lambda elmt: [elmt[0:k-1],elmt[1:k]]
DBG_edges = [edge(elmt) for elmt in DBG_edge_elmts]

temp = DBG_edges.pop(0)
cyclic = temp[0][-1]
while DBG_edges != []:
	cyclic += temp[1][-1]
	[index] = [i for i, pair in enumerate(DBG_edges) if pair[0] == temp[1]]
	temp = DBG_edges.pop(index)

with open('submit.txt', 'w') as output_file:
	output_file.write(cyclic)

#Ali Razzak

