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


    # Functions checks if matrix is made of zeroes and ones and if its in rectangular shape
    def check_matrix_appearance(self):
        for row in self.matrix:
            if len(row) != len(self.matrix[0]):
                return False

            for value in row:
                if value != '0' and value != '1':
                    return False

        return True


    # Function checks if it is possible to scan surrounding fields - sometimes those fields would be out of matrix range
    def check_move_possibility(self, field_row, field_column, row_change, column_change):
        if field_row + row_change < 0 or field_row + row_change == len(self.matrix):
            return False

        if field_column + column_change < 0 or field_column + column_change == len(self.matrix[0]):
            return False

        return True


    # Function is responsible for scanning surrounding fields and checking if they are ones - if so, it will then add such
    # fields to neighbours list
    def find_neighbours(self, field_row, field_column):
        moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        neighbours = []

        for move in moves:
            if self.check_move_possibility(field_row, field_column, move[0], move[1]):
                if self.matrix[field_row + move[0]][field_column + move[1]] == '1':
                    neighbours.append([field_row + move[0], field_column + move[1]])
                    
        return neighbours


    # This function is iteraiting over every single field of matrix and checks neighbours of each field. If no neighbours of 
    # the field being checked has been added to neighbours dict before, we can treat such field as a root - that means it is
    # the first piece of land of an island. Therefore later we can count how many roots we have to get the number of islands
    def find_number_of_islands(self):
        neighbours_dict = {}
        roots = []

        for row_index, columns in enumerate(self.matrix):
            for column_index, value in enumerate(columns):
                if value == '1':
                    duplicate = 0
                    neighbours = self.find_neighbours(row_index, column_index)

                    if neighbours == []:
                        if any([row_index, column_index] in neighbours_dict_value for neighbours_dict_value in neighbours_dict.values()):
                            duplicate = 1
                    elif neighbours != []:
                        for neighbour in neighbours:
                            if any(neighbour in neighbours_dict_value for neighbours_dict_value in neighbours_dict.values()):
                                duplicate = 1
                                break
                            
                            if duplicate == 0:
                                if any([row_index, column_index] in neighbours_dict_value for neighbours_dict_value in neighbours_dict.values()):
                                    duplicate = 1
                                    break

                    if duplicate == 0:
                        roots.append([row_index, column_index])

                    neighbours_dict[str([{row_index}, {column_index}])] = neighbours
                    self.matrix[row_index][column_index] = '0'

        return len(roots)
