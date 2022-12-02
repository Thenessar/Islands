import pytest
from islands import *

@pytest.fixture
def setUp():
    return Islands([])

def test_clean_the_matrix(setUp):
    test_argument = ['000\n', '101']
    setUp.matrix = test_argument
    expected = [['0', '0', '0'], ['1', '0', '1']]
    setUp.clean_the_matrix()
    actual = setUp.matrix
    message = f"clean_the_matrix({test_argument}) should return {expected}, but it actually returned {actual}"
    assert actual == expected, message


def test_check_matrix_appearance_shape(setUp):
    test_argument = ['0', '0', '0'], ['1', '0', '1']
    setUp.matrix = test_argument
    expected = True
    actual = setUp.check_matrix_appearance()
    message = f"check_matrix_appearance({test_argument}) should return {expected}, but it actually returned {actual}"
    assert actual == expected, message


def test_check_matrix_appearance_content(setUp):
    test_argument = ['0', '0', '0'], ['1', '0', '2']
    setUp.matrix = test_argument
    expected = False
    actual = setUp.check_matrix_appearance()
    message = f"check_matrix_appearance({test_argument}) should return {expected}, but it actually returned {actual}"
    assert actual == expected, message


def test_check_move_possibility(setUp):
    test_argument = (0, 0, -1, -1)
    expected = False
    actual = setUp.check_move_possibility(test_argument[0], test_argument[1], test_argument[2], test_argument[3])
    message = f"check_move_possibility{test_argument} should return {expected}, but it actually returned {actual}"
    assert actual == expected, message


def test_find_neighbours(setUp):
    test_argument = (1, 0)
    test_matrix = ['0', '0', '0'], ['1', '1', '0']
    setUp.matrix = test_matrix
    expected = [[1,1]]
    actual = setUp.find_neighbours(test_argument[0], test_argument[1])
    message = f"find_neighbours{test_argument} should return {expected}, but it actually returned {actual}"
    assert actual == expected, message


def test_find_number_of_islands(setUp):
    test_argument = [['0', '0', '0', '0', '0', '0', '0', '0', '0'], 
                     ['0', '1', '0', '0', '0', '0', '0', '0', '0'], 
                     ['1', '1', '1', '0', '0', '0', '1', '0', '0'], 
                     ['1', '1', '0', '0', '0', '1', '1', '1', '0'], 
                     ['0', '0', '0', '0', '0', '1', '1', '0', '0'], 
                     ['0', '0', '1', '0', '0', '0', '0', '0', '0'], 
                     ['1', '1', '0', '1', '0', '0', '0', '0', '0'], 
                     ['0', '0', '0', '0', '0', '1', '1', '0', '0']]

    setUp.matrix = test_argument
    expected = 4
    actual = setUp.find_number_of_islands()
    message = f"find_number_of_islands({test_argument}) should return {expected}, but it actually returned {actual}"
    assert actual == expected, message

