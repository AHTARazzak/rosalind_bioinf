'''
Title: Finding the Longest Multiple Repeat
Rosalind ID: LREP
URL: http://rosalind.info/problems/lrep
Goal: The longest substring of s that occurs at least k times in s. (If multiple solutions exist, you may return any single solution.)
'''
import sys

with open(sys.argv[1]) as input_data:
    raw_data = input_data.readlines()

s = raw_data[0].strip()
k = int(raw_data[1].strip())
node_info = [line.strip().split() for line in raw_data[2:]]
node_info = [[[line[0],line[1]], int(line[2]),int(line[3])]  for line in node_info]
edges = [info[0] for info in node_info]

previous_node = {'node1':'ROOT'}
for edge in edges:
    previous_node[edge[1]] = edge[0]

node_str = {'node1':''}
for info in node_info:
    node_str[info[0][1]] = s[info[1]-1:info[1]+info[2]-1].strip('$')

heads = set([edge[0] for edge in edges])
tails = set([edge[1] for edge in edges])
leaves = tails - heads

num_nodes = max([int(node[4:]) for node in leaves])
descendants = [0]*num_nodes
for leaf in leaves:
    descendants[int(leaf[4:])-1] += 1
    temp_node = previous_node[leaf]
    while temp_node != 'ROOT':
        descendants[int(temp_node[4:])-1] += 1
        temp_node = previous_node[temp_node]

candidate_nodes = list()
for i, num in enumerate(descendants[1:]):
    if num >= k:
        candidate_nodes.append('node'+str(i+2))

candidate_strings = list()
for node in candidate_nodes:
    temp_str = str()
    temp_node = node
    while temp_node != 'ROOT':
        temp_str = node_str[temp_node] + temp_str
        temp_node = previous_node[temp_node]
    candidate_strings.append(temp_str)

lrep = max(candidate_strings, key=len)
with open('submit.txt', 'w') as output_file:
    output_file.write(lrep)

#Ali Razzak
