import pytest
from leetcode.strangeprinter.solution import Solution

test_data = [('aaabbb', 2),
             ('aba', 2),
             ('abc', 3),
             ('abcabc', 5)]

@pytest.mark.parametrize("sequence, expected", test_data)
def test_strange_printer_should_return_minimum_number_of_operations(sequence, expected):
    solution = Solution()
    assert solution.strangePrinter(sequence) == expected