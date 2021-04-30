'''
Title: Completing a Tree
Rosalind ID: TREE
URL: http://rosalind.info/problems/tree
Goal: Calculate the minimum number of edges required to complete a tree with the provided adjacency matrix consisting of 'n' nodes. It is important to remember the 'n' nodes as some will have no connections at all.
'''
import sys

def get_most_overlap(s, L):
    most_string, most_overlap = "", ""
    for l in L:     
        overlap = ""
        for i in range(len(s)):
            if l[:len(s)-i] == s[:len(s)-i]:
                overlap = l[:len(s)-i]
                break
        if len(overlap) > len(most_overlap):
            most_string = l
            most_overlap = overlap
    return most_string, most_overlap

def get_adjacency_dict(strings):
    n = 1
    visited_string = []
    adjacency_dict = {}

    for s in strings:  
        # add first string to adjacency dict
        if len(visited_string) == 0:
            adjacency_dict[s] = []
            for i in range(len(s)):
                adjacency_dict[s].append([i + 1, i + 2, s[i]])
                n += 1
            visited_string.append(s)
            continue
        # if s is not the first string, and not in the visited_string, processing.
        if len(visited_string) > 0:
            most_string, most_overlap = get_most_overlap(s, visited_string)

            # if s not overlap with any visited strings
            if not most_overlap:
                adjacency_dict[s] = []
                adjacency_dict[s].append([1, n + 1, s[0]])
                n += 1
                for i in range(1, len(s)):
                    adjacency_dict[s].append([n, n + 1, s[i]])
                    n+=1
                visited_string.append(s)

            # if s overlap with any visited strings, get the most longest overlap string.
            if most_overlap:
                adjacency_dict[s] = []
                s_right = s[len(most_overlap):]

                adjacency_dict[s].extend(adjacency_dict[most_string][:len(most_overlap)])
                b = adjacency_dict[most_string][len(most_overlap)][0]
                adjacency_dict[s].append([b, n + 1, s_right[0]])
                n += 1
                for i in range(1, len(s_right)):
                    adjacency_dict[s].append([n, n + 1, s_right[i]])
                    n += 1
                visited_string.append(s)
    return adjacency_dict

with open(sys.argv[1], "r") as f:
    strings = [line.strip('\n') for line in f]

strings = sorted(strings, key=lambda x:len(x), reverse=True)
adjacency_dict = get_adjacency_dict(strings)
    
results = []
final_string = ""
for k, v in adjacency_dict.items():
    for b, e, s in v:
        if [b, e, s] not in results:
            results.append([b, e, s])
for b, e, s in results:     
    final_string += str(b) + " " + str(e) + " " + s + "\n"

outfile = open("submit.txt", "w")
outfile.write(final_string)
'''
import sys

all_seq = open(sys.argv[1], "r").read().split("\n")[:-1]

#all_seq = sorted(all_seq, key=len)[::-1]

the_dict = dict()

for i in range(len(all_seq[0])):
	the_dict[str(i + 1) + " " + str(i + 2)] = all_seq[0][i]

print(all_seq)

for i in all_seq[1:]:
	seq_switch = "F"
	for j in range(len(i)):
		try:
			if the_dict[str(j + 1)  + " " + str(j + 2)] != i[j]:
				if (j + 1) == 1:
					seq_switch = "T"
					the_dict[str(1)  + " " + str(len(the_dict) + 2)] = i[j]
				if seq_switch == "T":
					print("cool")
					print(i[j])
					the_dict[str(len(the_dict) + 1)  + " " + str(len(the_dict) + 2)] = i[j]
				else:
					the_dict[str(j + 1)  + " " + str(len(the_dict) + 2)] = i[j]
		except KeyError:
			the_dict[str(j + 1)  + " " + str(j + 2)] = i[j]

final_string = ""
for i in the_dict:
	final_string += (i + " " + the_dict[i]) + "\n"

outfile = open("submit.txt", "w")
outfile.write(final_string)

#Ali Razzak
'''