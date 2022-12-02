import sys
from islands import *


# Read file from input and divide the text in lines (those will be our rows)
file = open(sys.argv[1], 'r')
rows = file.readlines()

# Create object
my_islands = Islands(rows)

# Clean the data - get rid of new line symbols
my_islands.clean_the_matrix()

# Check if the matrix is rectangle and is made of zeroes and ones
if not my_islands.check_matrix_appearance():
    raise Exception("Matrix Appearance Error: Matrix has to be made of zeroes and ones and be in a rectangular shape")

# Find the number of islands :)
stdout = my_islands.find_number_of_islands()

# Print the result
print(stdout)