import sys

the_data_string =  open(sys.argv[1]).read().split()[0]

AA_chance = open(sys.argv[1]).read().split("\n")[5].split()[1]
AB_chance = open(sys.argv[1]).read().split("\n")[6].split()[1]
BA_chance = open(sys.argv[1]).read().split("\n")[5].split()[2]
BB_chance = open(sys.argv[1]).read().split("\n")[6].split()[2]


the_pair = []
prob = 1
for i in range(len(the_data_string)):
	if i == 0:
		the_pair.append(the_data_string[i])
	else:
		the_pair.append(the_data_string[i])
		if "".join(the_pair) == "AA":
			prob = prob * float(AA_chance)
		elif "".join(the_pair) == "AB":
			prob = prob * float(AB_chance)
		elif "".join(the_pair) == "BA":
			prob = prob * float(BA_chance)
		else:
			prob = prob * float(BB_chance)
		print(the_pair)
		the_pair.pop(0)


print(prob)
