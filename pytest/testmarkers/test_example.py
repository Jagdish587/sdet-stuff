import pytest

@pytest.mark.setexample
def test_file_example1():
    input_value = 5
    assert input_value*5 == 25


def test_file_example1_a():
    input_value = 6
    assert input_value*5 == 25