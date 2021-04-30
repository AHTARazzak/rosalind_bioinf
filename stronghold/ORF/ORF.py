'''
Title: Open Reading Frames
Rosalind ID: ORF
URL: http://rosalind.info/problems/orf
Goal: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
'''

from Bio import SeqIO
import re
import sys

def translate(seq):
      
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein =""
    if len(seq)%3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein+= table[codon]
    return protein

def get_complement_strand(this_sequence):
	nucleotide_allowed = ["A", "T", "G", "C"]
	complement_sequence = ""
	for nucleotide in the_sequence:
		if nucleotide in nucleotide_allowed:
			if nucleotide == "A":
				complement_sequence += "T"
			elif nucleotide == "T":
				complement_sequence += "A"
			elif nucleotide == "G":
				complement_sequence += "C"
			elif nucleotide == "C":
				complement_sequence += "G"
	return(complement_sequence)

protein_list_bad = []
protein_list_good = []

final_list = open("output_file.txt", "w")

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		the_sequence = (str(record.seq))
		start_codon_list = [m.start() for m in re.finditer(r"(?=(ATG))", the_sequence)]
		stop_codon_list = [m.start() for m in re.finditer(r"(?=(TAA|TGA|TAG))", the_sequence)]
		for start_place in start_codon_list:
			for stop_place in stop_codon_list:
				if start_place < stop_place:
					if (((stop_place - start_place) % 3) ==0):
						protein_list_bad.append(translate(the_sequence[start_place:stop_place]))
		reverse_sequence = get_complement_strand(the_sequence)[::-1]
		start_codon_list = [m.start() for m in re.finditer(r"(?=(ATG))", reverse_sequence)]
		stop_codon_list = [m.start() for m in re.finditer(r"(?=(TAA|TGA|TAG))", reverse_sequence)]
		for start_place in start_codon_list:
			for stop_place in stop_codon_list:
				if start_place < stop_place:
					if (((stop_place - start_place) % 3) ==0):
						protein_list_bad.append(translate(reverse_sequence[start_place:stop_place]))
		protein_list_good = []
		final_string = ""
		for protein in protein_list_bad:
			if "_" not in protein:
				if (protein) not in protein_list_good:
					protein_list_good.append(protein)
					final_string += protein + "\n"

print(final_string)
final_list.write(final_string)
#Ali Razzak