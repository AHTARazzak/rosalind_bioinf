'''
Title: Distances in Trees
Rosalind ID: NWCK
URL: http://rosalind.info/problems/nwck
Goal: A collection of n positive integers, for which the kth integer represents the distance between xk and yk in Tk.
'''

import sys

def dis_tree(T, x, y):
    x_index = T.find(x)
    y_index = T.find(y)
    t = [i for i in T[min(x_index, y_index):max(x_index, y_index)] if i in [')','(',',']]
    bracket = ''
    for i in t:
        bracket += i
    while '(,)' in bracket:
        bracket = bracket.replace('(,)','')
    if bracket.count('(') == len(bracket):
        return len(bracket)
    elif bracket.count(')') == len(bracket):
        return len(bracket)
    elif bracket.count(',') == len(bracket):
        return 2
    else:
        return bracket.count(')') + bracket.count('(') + 2

with open(sys.argv[1], 'r') as f:
	tree = [line.strip().replace(';','') for line in f.readlines() if len(line.strip()) > 0]
for i in range(0, len(tree), 2):
	T = tree[i]
	x, y = tree[i+1].split(' ')
	print(dis_tree(T, x, y), end=" ")
#Ali Razzaks