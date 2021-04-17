stat_file = input("Name of file please: ")
open_stat = open(stat_file, 'r')
the_stats = open_stat.read()

coupling_list_str = the_stats.split()
coupling_list_int = []

for stat_string in coupling_list_str:
	coupling_list_int.append(int(stat_string))

parent_num = (sum(coupling_list_int))
offspring_num = (sum(coupling_list_int)) * 2

if coupling_list_int[0] > 0:
	off_spring_dom_chance = coupling_list_int[0] / parent_num
if coupling_list_int[1] > 0:
	off_spring_dom_chance += coupling_list_int[1] / parent_num
if coupling_list_int[2] > 0:
	off_spring_dom_chance += coupling_list_int[2] / parent_num
if coupling_list_int[3] > 0:
	off_spring_dom_chance += 0.75 * (coupling_list_int[3] / parent_num)
if coupling_list_int[4] > 0:
	off_spring_dom_chance += 0.5 * (coupling_list_int[4] / parent_num)



print(round(off_spring_dom_chance * offspring_num, 1))