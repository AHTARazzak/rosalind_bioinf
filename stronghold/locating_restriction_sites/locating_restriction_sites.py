from Bio import SeqIO
import re
import sys

palindrone_initiate = ["AATT", "TATA", "GATC", "CATG", "TTAA", "ATAT", "GTAC", "CTAG", "GGCC", "CGCG", "AGCT", "TGCA", "CCGG", "GCGC", "AGCT", "TGCA"]
palindrone_pairs = ["AT", "TA", "GC", "CG"]
all_palindrone = []
no_duplicates_palindrone_raw = []
amount_cut = 0

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		the_sequence = (str(record.seq))
		pos_palindrone = ([m.start()+1 for m in re.finditer(r"(?=(AATT|TATA|GATC|CATG|TTAA|ATAT|GTAC|CTAG|GGCC|CGCG|AGCT|TGCA|CCGG|GCGC|ACGT|TCGA))", the_sequence)])
		for this_palindrone in pos_palindrone:
			check_next = 2
			palin_length = 4
			for i in range(4):
				if ((this_palindrone - check_next) > -1) and ((this_palindrone + check_next + 1) < len(the_sequence)):
					if (the_sequence[(this_palindrone - check_next)] + the_sequence[(this_palindrone + check_next + 1)]) in palindrone_pairs:
						check_next += 1
						palin_length += 2
					else:
						all_palindrone.append(str(this_palindrone) + "\t" + str(palin_length))
				else:
					all_palindrone.append(str(this_palindrone) + "\t" + str(palin_length))

[no_duplicates_palindrone_raw.append(x) for x in all_palindrone if x not in no_duplicates_palindrone_raw]

print(no_duplicates_palindrone_raw)

adjusted_pali = []
old_excluded_list = []
for raw_palindrone in no_duplicates_palindrone_raw:
	pali_pos = int(raw_palindrone.split()[0])
	pali_length = int(raw_palindrone.split()[1])
	if pali_length > 4:
		adjusted_pali.append(str(pali_pos) + "\t" + str(4))
		for add_pali in range(int((pali_length - 4) / 2)):
			adjusted_pali.append(str(pali_pos - (add_pali + 1)) + "\t" + str((4 + ((add_pali + 1 ) * 2))))
	else:
		old_excluded_list.append(str(pali_pos) + "\t" + str(pali_length))

final_list = (adjusted_pali + old_excluded_list)

comb_file = open("sub_file.txt", "a")
for i in final_list:
	comb_file.write(i + "\n")

#TCAGATCATGCGGGTCTATATGCAT