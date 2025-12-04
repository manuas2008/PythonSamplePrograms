from PythonSamplePrograms.base7 import convertToBase7
import pytest
@pytest.mark.parametrize(
    "num, expected",
    [
        (100, 202),
        (7, 10),
        (0, 0),
        (1, 1),
        (50, 101),
        (343, 1000),
        (-10, -13),
    ],
    ids=[
        "base10_100",
        "base10_7",
        "base10_0",
        "base10_1",
        "base10_50",
        "base10_343",
        "negative_number",
    ],
)
def test_convertToBase7(num, expected):
    assert convertToBase7(num) == expected
    