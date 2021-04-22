'''
Problem Title: Longest Increasing Subsequence
Rosalind ID: LGIS
URL: http://rosalind.info/problems/lgis/
'''
from math import ceil
import sys
import os

def BS(S, data, value):
	original_S = S
	while len(S) > 1:
		index = int(ceil(len(S) / 2.0 - 1))
		if data[S[index]] < value:
			S = S[index + 1:]
		else:
			S = S[:index + 1]
	return original_S.index(S[0])

def LongestIncSubstring(data):
	S = [0]
	parent = [None]*len(data)
	for index in range(1,len(data)):
		if data[index] > data[S[len(S) - 1]]:
			parent[index] = S[len(S) - 1]
			S.append(index)
		else:
			update_index = BS(S, data, data[index])
			S[update_index] = index
			parent[index] = S[update_index - 1]

	LIS = [S[len(S) - 1]]
	for i in range(0,len(S) - 1):
		LIS.append(parent[LIS[len(LIS)-1]])

	LIS = [data[i] for i in LIS]
	LIS.reverse()
	return LIS



f =  open(os.path.join(os.path.split(os.getcwd())[0],"LGIS", sys.argv[1]), 'r')
    
data = [map(int, line.rstrip().split()) for line in f.readlines()]
n = data.pop(0)
perm = data.pop(0)
f.close()

LIS = map(str, LongestIncSubstring(perm))

negperm = [-1*i for i in perm]
LDS = map(str, [-1*i for i in LongestIncSubstring(negperm)])

outputhandle = open(os.path.join(os.path.split(os.getcwd())[0],"LGIS", "submit.txt"),'w')
outputhandle.write(' '.join(LIS) + '\n')
outputhandle.write(' '.join(LDS))
outputhandle.close()