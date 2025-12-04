from PythonSamplePrograms.isSubSequence import is_subsequence
import pytest
@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("abc", "aabchbgdc", True),
        ("axc", "ahbgdc", False),
        ("", "ahbgdc", True),
        ("abc", "", False),
        ("ace", "abcde", False),
        ("aec", "abcde", False),
    ],
    ids=[
        "subsequence_present",
        "subsequence_absent",
        "empty_s1",
        "empty_s2",
        "non_consecutive_subsequence",
        "wrong_order_subsequence",
    ],
)
def test_is_subsequence(s1, s2, expected):
    assert is_subsequence(s1, s2) == expected
