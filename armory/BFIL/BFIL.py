'''
Base Filtration by Quality
Rosalind ID: BFIL
http://rosalind.info/problems/bfil/
Goal: FASTQ file trimmed from the both ends (removed leading and trailing bases with quality lower than q)
'''
from Bio import SeqIO
import statistics
import sys

the_threshold = int(open(sys.argv[1], "r").readlines()[0].split("\n")[0])

fastq_open = open("cool.txt", "w")
fastq_open.write("".join(open(sys.argv[1], "r").readlines()[1:]))
fastq_open.close()

positions = []

with open("cool.txt") as fastq_file:
	for record in SeqIO.parse(fastq_file, "fastq"):
		forward_position = 0
		backward_position = 0
		spots = []
		for qual in record.letter_annotations["phred_quality"]:
			if qual < the_threshold:
				spots.append("a")
			else:
				spots.append("b")
		if "".join(spots).find("a") < "".join(spots).find("b"):
			forward_position =  "".join(spots).find("b")
		if "".join(spots[::-1]).find("a") < "".join(spots[::-1]).find("b"):
			backward_position =  "".join(spots[::-1]).find("b")
		if backward_position == 0:
			positions.append(str(forward_position) + " " + str(-1))
		else:
			positions.append(str(forward_position) + " " + str((backward_position) * -1))
		print("".join(spots))
print(positions)

fastq_read = open("cool.txt", "r").read().split("\n")[:-1]

chunk_file = [fastq_read[i:i + 4] for i in range(0, len(fastq_read), 4)]

final_string = ""

for i in range(len(chunk_file)):
	for element in range(len(chunk_file[i])):
		if (element == 1) or (element == 3):
			final_string += (chunk_file[i][element][int(positions[i].split()[0]):int(positions[i].split()[1])]) + "\n"
		else:
			final_string += chunk_file[i][element] + "\n"

final_file = open("submit.txt", "w")

final_file.write(final_string)

#Ali Razzak