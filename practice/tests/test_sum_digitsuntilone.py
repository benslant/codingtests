from sumdigitsuntilone.solution import seek_single_digit_sum
import pytest

testdata = [
    (49, 4),
    (100, 1),
    (500, 5),
    (10009, 1),
    (10019, 2),
    (439230, 3)
]

@pytest.mark.parametrize("number,expected", testdata)
def test_should_return_single_digit_result(number: int, expected: int):
    assert seek_single_digit_sum(number) == expected