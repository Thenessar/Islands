from islands import *

file = open('islands.txt', 'r')
lines = file.readlines()

my_islands = Islands(lines)
my_islands.clean_the_matrix()
my_islands.check_matrix_appearance()
stdout = my_islands.find_number_of_islands()

print(stdout)