from typing import List
import pytest
from nextlargernumbers.solution import next_larger_number

test_data = [([3,1,3,4], [4,3,4,-1])]

@pytest.mark.parametrize("array, expected", test_data)
def test_should_find_largest_adjecent_value(array: List[int], expected: List[int]):
    assert next_larger_number(array) == expected