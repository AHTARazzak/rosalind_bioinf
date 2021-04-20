from scipy.special import binom
import sys

pop_file = open(sys.argv[1], 'r')
break_numbers = pop_file.read().split()



def des_function(generation, number_observed):
	def p(number_obs, generation):
		return binom(2**generation, number_obs) * 0.25**number_obs * 0.75**(2**generation - number_obs)
	return 1 - sum(p(n, generation) for n in range(number_observed))

print(round(des_function(int(break_numbers[0]), int(break_numbers[1])), 3))
