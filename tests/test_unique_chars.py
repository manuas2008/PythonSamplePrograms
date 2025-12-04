from PythonSamplePrograms.unique_chars import unique_chars
import pytest

@pytest.mark.parametrize(
    "s, expected",
    [
        ("aabcEdfg", False),
        ("abcdef", True),
        ("", True),
        ("1234567890", True),
        ("112233", False),
    ],
    ids=["duplicate_letters", "all_unique", "empty_string", "numeric_unique", "numeric_duplicates"],
)
def test_unique_chars(s, expected):
    assert unique_chars(s) == expected