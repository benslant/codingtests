import pytest
from slalom.setup_test import multiply_by_two

def test_should_multiply_by_two():
    assert multiply_by_two(2) == 4

def test_should_equal_four():
    assert multiply_by_two(2) != 3