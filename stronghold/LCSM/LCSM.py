'''
Title: Finding a Shared Motif
Rosalind ID: LCSM
URL: http://rosalind.info/problems/lcsm
Goal: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
'''

from Bio import SeqIO                      
sequences = []                             
handle = open('rosalind_lcsm.txt', 'r')
for record in SeqIO.parse(handle, 'fasta'):
    sequence = []                          
    seq = ''                               
    for nt in record.seq:                  
        seq += nt                          
    sequences.append(seq)                  
handle.close()
#Search through the haystack and return the output:

srt_seq = sorted(sequences, key=len)     
short_seq = srt_seq[0]                   
comp_seq = srt_seq[1:]                   
motif = ''                               
for i in range(len(short_seq)):          
    for j in range(i, len(short_seq)):   
        m = short_seq[i:j + 1]           
        found = False                   
        for sequ in comp_seq:            
            if m in sequ:                
                found = True            
            else:                        
                found = False           
                break                   
        if found and len(m) > len(motif):
            motif = m                    
print(motif)

#Ali Razzak

'''
#s.system("clustalo -i " + sys.argv[1] + " --outfmt=clu -o output_file.txt --force")
clustalo_file = open("output_file.txt", 'r')

record_list = []
id_list = []
astrix_line = ""

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		record_list.append(str(record.seq))
		test_id = record.id

record_lengths = [len(x) for x in record_list]
index_longest_rec = record_lengths.index(max(record_lengths))
longest_rec = record_list[index_longest_rec]

empty_lines = 0

for line in clustalo_file.readlines():
	if "*" in line:
		astrix_line += line[(len(test_id) + 6):-1]

kill_string 

clustalo_file.close()
clustalo_file = open("output_file.txt", 'r')
for line in clustalo_file.readlines()[4:]:
	if "*" in line:
		break
	else:
		if line == "\n":
			empty_lines += 1
		if test_id in line:



empty_spaces = (empty_lines) * (81 - len(test_id) + 6 )

print((int(empty_spaces) * " ") + astrix_line)

atrix_split = astrix_line.split()
astrix_length = [len(x) for x in atrix_split]
shortest_mot_start = int(empty_spaces) + (astrix_line.find((min(astrix_length) * "*")))
shortest_mot_end = shortest_mot_start + min(astrix_length)

print(shortest_mot_start)
print(shortest_mot_end)
print(longest_rec[shortest_mot_start : shortest_mot_end])

poo_file = open("fun.txt", "a")

[(poo_file.write(x + "\n")) for x in record_list]
'''