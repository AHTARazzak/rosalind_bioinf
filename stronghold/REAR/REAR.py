'''
Title: Reversal Distance
Rosalind ID: REAR
URL: http://rosalind.info/problems/rear
Goal: The reversal distance between each permutation pair.
'''

import sys

def _get_reverse_array(s):
    reverse_arrays = list()
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            r_list = s[i:j+1]
            r_list.reverse()
            reverse_arrays.append(s[:i] + r_list + s[j+1:])
    return reverse_arrays

def _get_reversal_distance(s1, s2, distance):
    if s1 & s2:
        return distance
    new_s1 = set()
    for s in s1:
        reverse_arrays = _get_reverse_array(list(s))
        for r in reverse_arrays:
            new_s1.add(tuple(r))
    new_s2 = set()
    for s in s2:
        reverse_arrays = _get_reverse_array(list(s))
        for r in reverse_arrays:
            new_s2.add(tuple(r))
    distance += 2
    if s1 & new_s2:
        return distance-1
    if s2 & new_s1:
        return distance-1
    if new_s1 & new_s2:
        return distance
    
    distance = _get_reversal_distance(new_s1, new_s2, distance)
    return distance


with open(sys.argv[1], "r") as f:
	lines = [line.strip().split(" ") for line in f.readlines() if line.strip()]
for i in range(0, len(lines), 2):
	a = [l for l in lines[i]]
	b = [l for l in lines[i+1]]
	distance, s1, s2 = 0, set(), set()
	s1.add(tuple(a)), s2.add(tuple(b))
	d = _get_reversal_distance(s1, s2, distance)
	print(d)