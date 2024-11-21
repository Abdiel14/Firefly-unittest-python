import pytest
from max_num_finder import find_max

def test_find_max():
    # Testing positive list numbers
    assert find_max([1,2,3,4,5,6,7]) == 7

    # Testing negative list numbers
    assert find_max([-1, -2, -3, -4, -5]) == -1

    # Testing float list numbers
    assert find_max([0.1, 0.2, 0.3, 0.4, 0.5]) == 0.5
   
    # Testing empty list
    assert find_max([]) == None