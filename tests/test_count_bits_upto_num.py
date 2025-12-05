from PythonSamplePrograms.count_bits_upto_num import count_bits_upto_num
import pytest
@pytest.mark.parametrize(
    "num, expected",
    [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (0, [0]),
        (1, [0, 1]),
        (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
        (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]),
    ],
    ids=[
        "num_2",
        "num_5",
        "num_0",
        "num_1",
        "num_8",
        "num_10",
    ],
)
def test_count_bits_upto_num(num, expected):
    assert count_bits_upto_num(num) == expected 
    