import sys
import re

data_file = open(sys.argv[1], "r")
data_content = data_file.read().split("\n")
num_nodes = data_content[0]
pathing = data_content[1:]

cluster_dict = {}
dict_num = 0
numbers_of_clusters = ["0"] * int(num_nodes)

print(numbers_of_clusters)

for row in pathing:
	if len(row) > 0:
		cluster_dict[row.split()[0]] = row.split()[1]

for entry in cluster_dict:
	print(entry)
