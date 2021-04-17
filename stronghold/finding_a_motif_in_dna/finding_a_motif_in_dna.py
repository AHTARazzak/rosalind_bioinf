the_content_file = input("Name of file please: ")
the_file_content = open(the_content_file, 'r')
the_content = the_file_content.read().split()

the_sequence = the_content[0]
the_motif = the_content[1]

positions_found = [0]

search_seq = the_sequence

while search_seq.find(the_motif) > 0:
	positions_found.append(search_seq.find(the_motif) + 1 + positions_found[-1])
	search_seq = search_seq[search_seq.find(the_motif) + 1 :]

final_string = ""

for i in positions_found[1:]:
	final_string += str(i) + " "

print(final_string)