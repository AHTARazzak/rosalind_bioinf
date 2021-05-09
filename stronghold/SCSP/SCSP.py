'''
Title: Interleaving Two Motifs
Rosalind ID: SCSP
URL: http://rosalind.info/problems/scsp
Goal: A shortest common supersequence of s and t. If multiple solutions exist, you may output any one.
'''
import sys
import pprint

def SCS(s1, s2):
	m, n = len(s1), len(s2)
	DP = [[0]*(n+1) for i in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				DP[i][j] = 0
			elif s1[i-1] == s2[j-1]:
				DP[i][j] = DP[i-1][j-1]+1
			else:
				DP[i][j] = max(DP[i-1][j], DP[i][j-1])

	scs = ""
	i, j = len(s1), len(s2)
	while (i>0 or j>0):
		if DP[i][j] == DP[i-1][j]:
			i -= 1
			scs = s1[i]+scs
		elif DP[i][j] == DP[i][j-1]:
			j -= 1
			scs = s2[j]+scs
		else:
			scs = s1[i-1]+scs
			i -= 1
			j -= 1
	print(scs)
	return DP[m][n]

the_file = open(sys.argv[1], "r")

sequences = the_file.readlines()
seq_1 = (sequences[0].strip()) 
seq_2 = (sequences[1].strip()) 
res = SCS(seq_1, seq_2)
'''
the_file = open(sys.argv[1], "r")

sequences = the_file.readlines()

seq_1 = (sequences[0].strip()) 
seq_2 = (sequences[1].strip()) 

both_sequences = [seq_1,seq_2]
both_sequences.sort(key=len)

longer_seq = both_sequences[1]
shorter_seq = both_sequences[0]

switch_1 = 1
switch_2 = 0
backpush = 0
the_string = str()
for i in range(len(longer_seq)):
	if len(seq_1) > len(seq_2):
		if i < len(seq_2):
			if switch_1 == 1:
				if seq_1[i] != seq_2[i]:
					the_string += seq_1[i]
				else:
					switch_1 = 0
					switch_2 = 1
					the_string += seq_2[i-1] + seq_2[i]
			else:
				if seq_2[i] != seq_1[i]:
					the_string += seq_2[i]
				else:
					switch_1 = 1
					switch_2 = 0
					the_string += seq_1[i-1] + seq_1[i]
		else:
			the_string += seq_1[i]
	else:
		if i < len(seq_1):
			if switch_1 == 1:
				if seq_1[i] != seq_2[i]:
					the_string += seq_1[i]
				else:
					switch_1 = 0
					switch_2 = 1
					the_string += seq_2[i-1] + seq_2[i]
			else:
				if seq_2[i] != seq_1[i]:
					the_string += seq_2[i]
				else:
					switch_1 = 1
					switch_2 = 0
					the_string += seq_1[i-1] + seq_1[i]
		else:
			the_string += seq_2[i]


print(the_string)
'''

#Ali Razzak