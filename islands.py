class Islands:
    def __init__(self, matrix):
        self.matrix = matrix


    def clean_the_matrix(self):
        tmp_matrix = []

        for row in self.matrix:
            tmp_matrix.append(list(row.rstrip('\n')))
        
        self.matrix = tmp_matrix


    def check_matrix_appearance(self):
        for row in self.matrix:
            if len(row) != len(self.matrix[0]):
                return False

            for value in row:
                if value != '0' and value != '1':
                    return False

        return "Rectangle"


    def check_move_possibility(self, field_row, field_column, row_change, column_change):
        if field_row + row_change < 0 or field_row + row_change == len(self.matrix):
            return False

        if field_column + column_change < 0 or field_column + column_change == len(self.matrix[0]):
            return False

        return True


    def find_neighbours(self, field_row, field_column):
        moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        neighbours = []

        for move in moves:
            if self.check_move_possibility(field_row, field_column, move[0], move[1]):
                if self.matrix[field_row + move[0]][field_column + move[1]] == '1':
                    neighbours.append([field_row + move[0], field_column + move[1]])
        return neighbours


    def find_number_of_islands(self):
        roots = {}

        for row_index, columns in enumerate(self.matrix):
            for column_index, value in enumerate(columns):
                if value == '1':
                    roots[f"[{row_index},{column_index}]"] = self.find_neighbours(row_index, column_index)
                    self.matrix[row_index][column_index] = 0
        
        result = list(filter(lambda x: x == [], roots.values()))
        return len(result)
