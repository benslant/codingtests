import pytest
from typing import List
from maxproductthreenumbers.solution import max_product_of_three

test_data = [([-1,9,22,3,-15,-7], 2310),
             ([0, 1, 2, 3], 6),
             ([-12, -7, -1, 11, 17], 1428),
             ([-12, -7, 17], 1428),
             ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 504)]

@pytest.mark.parametrize("numbers,expected", test_data)
def test_max_product_three_numbers(numbers: List[int], expected: int):
    assert max_product_of_three(numbers) == expected