from math import factorial
import sys

the_data = open(sys.argv[1], 'r')
max_num, max_digits = map(int, the_data.readline().split())

solution = (factorial(max_num) / factorial(max_num - max_digits)) % 1000000
print(solution)