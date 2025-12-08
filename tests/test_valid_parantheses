from PythonSamplePrograms.valid_parantheses import is_valid_parantheses
import pytest  
@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        (")(", False),
        ("((()))", True),
        ("{[()()]}", True),
        ("{[(])}", False),
    ],
    ids=[
        "simple_valid_1",
        "simple_valid_2",
        "mismatched_1",
        "mismatched_2",
        "nested_valid",
        "empty_string",
        "closing_before_opening",
        "multiple_nested_valid",
        "complex_nested_valid",
        "complex_mismatched",
    ],
)
def test_is_valid_parantheses(s, expected):
    assert is_valid_parantheses(s) == expected
    