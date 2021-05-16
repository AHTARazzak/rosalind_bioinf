'''
Title: Sorting by Reversals
Rosalind ID: SORT
URL: http://rosalind.info/problems/sort
Goal: The reversal distance drev(π,γ), followed by a collection of reversals sorting π into γ. If multiple collections of such reversals exist, you may return any one.
'''
import random
import sys

def _get_reverse_array(s):
    reverse_arrays = []
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            r_list = s[i:j+1]
            r_list.reverse()
            reverse_arrays.append(s[:i] + r_list + s[j+1:])
    return reverse_arrays

def _get_reversal_distance(s1, s2, distance, s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals):
    if s1 & s2:
        return s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance
    new_s1 = set()
    s1_s2 = {}
    for s in s1:
        reverse_arrays = _get_reverse_array(list(s))
        s1_s2[s] = reverse_arrays
        for r in reverse_arrays:
            new_s1.add(tuple(r))
    s1_s2_reversals_path.append(s1_s2)
    new_s2 = set()
    s2_s1 = {}
    for s in s2:
        reverse_arrays = _get_reverse_array(list(s))
        s2_s1[s] = reverse_arrays
        for r in reverse_arrays:
            new_s2.add(tuple(r))
    s2_s1_reversals_path.append(s2_s1)
    distance += 2
    if s1 & new_s2:
        meet_reversals = list(s1 & new_s2)
        return s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance-1
    if s2 & new_s1:
        meet_reversals = list(s2 & new_s1)
        return s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance-1
    if new_s1 & new_s2:
        meet_reversals = list(new_s1 & new_s2)
        return s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance
    
    s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance = _get_reversal_distance(new_s1, new_s2, distance, s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals)
    return s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance

def _get_invert_endpoints(a, b):
    a_reverse = []
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            a_reverse = a[:i] + a[i:j+1][::-1] + a[j+1:]
            if a_reverse == b:
                return i+1, j+1

def _get_collections_of_reversals_sorting(s1_s2_reversals_path, meet_reversals, s2_s1_reversals_path):
    collections_of_reversals_sorting = []
    for l in meet_reversals:
        collection_of_reversals_sorting=[]
        current_array = list(l)
        for reversals_path in s1_s2_reversals_path[::-1]:
            for k, v in reversals_path.items():
                if current_array in v:
                    i, j =  _get_invert_endpoints(list(k), current_array)
                    collection_of_reversals_sorting.append([i, j])
                    current_array = list(k)
                    break
        collection_of_reversals_sorting = collection_of_reversals_sorting[::-1]
        current_array = list(l)
        for reversals_path in s2_s1_reversals_path[::-1]:
            for k, v in reversals_path.items():
                if current_array in v:
                    i, j =  _get_invert_endpoints(list(k), current_array)
                    collection_of_reversals_sorting.append([i, j])
                    current_array = list(k)
                    break
        collections_of_reversals_sorting.append(collection_of_reversals_sorting)
    return collections_of_reversals_sorting
            

a = open(sys.argv[1], 'r').read().split("\n")[0]
b = open(sys.argv[1], 'r').read().split("\n")[1]

distance, s1, s2 = 0, set(), set()
s1.add(tuple(a)), s2.add(tuple(b))
s1_s2_reversals_path = []
s2_s1_reversals_path = []
meet_reversals = []
s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals, distance = _get_reversal_distance(s1, s2, distance, s1_s2_reversals_path, s2_s1_reversals_path, meet_reversals) # 4
print("[INFO] the distance of reverse s1 to s2: {}".format(distance))
    
collections_of_reversals_sorting = _get_collections_of_reversals_sorting(s1_s2_reversals_path, meet_reversals, s2_s1_reversals_path)
print("[INFO] the number of collections of reversals sorting π into γ: {}".format(len(collections_of_reversals_sorting)))
a_collection = random.sample(collections_of_reversals_sorting, k=1)[0]
print("[INFO] the reversal distance drev(π,γ): {}".format(len(a_collection)))
print("A random collection of reversals sorting π into γ:")
print(a_collection)
print("done!")

#Ali Razzak
