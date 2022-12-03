# This class presents an object that contains a matrix made of zeroes and ones
class Islands:
    def __init__(self, matrix):
        self.matrix = matrix


    # Function gets rid of new line symbols
    def clean_the_matrix(self):
        tmp_matrix = []

        for row in self.matrix:
            tmp_matrix.append(list(row.rstrip('\n')))
        
        self.matrix = tmp_matrix


    # Functions checks if matrix is made of zeroes and ones and if its in a rectangular shape
    def check_matrix_appearance(self):
        for row in self.matrix:
            if len(row) != len(self.matrix[0]):
                return False

            for value in row:
                if value != '0' and value != '1':
                    return False

        return True


    # Function checks if it is possible to scan surrounding fields - sometimes those fields would be out of matrix's range
    def check_move_possibility(self, field_row, field_column, row_change, column_change):
        if field_row + row_change < 0 or field_row + row_change == len(self.matrix):
            return False

        if field_column + column_change < 0 or field_column + column_change == len(self.matrix[0]):
            return False

        return True


    # Function is responsible for scanning surrounding fields and checking if they are ones - if so, it will then
    # recursively check surrounding fields while changing their value to zero (to make sure we dont check the same
    # field more than once) untill there is none left. That means we have fully explored the island.
    def explore_island(self, field_row, field_column):
        moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        for move in moves:
            if self.check_move_possibility(field_row, field_column, move[0], move[1]):
                if self.matrix[field_row + move[0]][field_column + move[1]] == '1':
                    self.matrix[field_row + move[0]][field_column + move[1]] = '0'
                    self.explore_island(field_row + move[0], field_column + move[1])


    # This function is iteraiting over every single field of matrix in search of ones. After finding such field it
    # will change it's value to 0 and increase the number of islands found. Finally it will start exploring the island.
    # After we scanned the whole "map", we can print the number of islands.
    def find_number_of_islands(self):
        number_of_islands = 0

        for row_index, columns in enumerate(self.matrix):
            for column_index, value in enumerate(columns):
                if value == '1':
                    number_of_islands += 1
                    self.matrix[row_index][column_index] = '0'
                    self.explore_island(row_index, column_index)

        return number_of_islands

