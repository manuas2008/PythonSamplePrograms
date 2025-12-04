from PythonSamplePrograms.sorted_or_not import sorted_or_not
import pytest

@pytest.mark.parametrize(
    "arr, expected",   
    [
        ([1, 2, 3, 4, 5, 6], True),
        ([1, 2, 5, 8, 2, 3], False),
        ([7, 6, 5, 4, 3, 2, 1], True),
        ([], True),
        ([42], True),
        ([3, 3, 3, 3], True),
    ],
)
def test_sorted_or_not(arr, expected):
    assert sorted_or_not(arr) == expected   