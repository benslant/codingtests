import pytest
from matrixoperations.solution import IncrementOp
from matrixoperations.solution import matrixoperations

test_data = [(4,4,[IncrementOp(1,1), IncrementOp(2,2)], 1),
             (4,4,[IncrementOp(1,1), IncrementOp(2,2), IncrementOp(3,3)], 1)]

@pytest.mark.parametrize("rows, columns, operations, expected", test_data)
def test_matrix_operations(rows, columns, operations, expected):
    assert matrixoperations(rows, columns, operations) == expected