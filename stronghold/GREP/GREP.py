'''
Title: Genome Assembly with Perfect Coverage and Repeats
Rosalind ID: GREP
URL: http://rosalind.info/problems/grep
Goal: All circular strings assembled by complete cycles in the de Bruijn graph Bk of Sk+1. The strings may be given in any order, but each one should begin with the first (k+1)-mer provided in the input.
'''
import sys

def coverings(s, edges, k):
	add_on = [index for index, item in enumerate(edges) if item[0] == s[-k+1:]]

	if len(add_on) == 0:
		return [s if edges == [] else []]
	else:
		return [coverings(s+edges[i][1][-1], edges[:i]+edges[i+1:], k) for i in add_on]

def flatten(lst):
	for element in lst:
		if isinstance(element, list):
			for subelement in flatten(element):
				yield subelement		
		else:
			yield element

if __name__ == '__main__':

	with open(sys.argv[1]) as input_data:
		k_mers = [line.strip() for line in input_data.readlines()]

	k = len(k_mers[0])
	edge = lambda elmt: [elmt[0:k-1],elmt[1:k]]
	DBG_edges = [edge(elmt) for elmt in k_mers[1:]]

	circular_strings = [circular[:len(k_mers)] for circular in set(flatten(coverings(k_mers[0], DBG_edges, k)))]

	print ('\n'.join(circular_strings))
	with open('submit.txt', 'w') as output_data:
		output_data.write('\n'.join(circular_strings))

#Ali Razzak