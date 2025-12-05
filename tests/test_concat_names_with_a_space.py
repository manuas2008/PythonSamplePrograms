from PythonSamplePrograms.concat_names_with_a_space import concat_names_with_a_space
import pytest
@pytest.mark.parametrize(
    "names, expected",
    [
        (["John", "Doe"], "John Doe"),
        (["Alice", "Smith"], "Alice Smith"),
        (["", "Brown"], " Brown"),
        (["Emily", ""], "Emily "),
        (["", ""], " "),
        (["SingleName"], "SingleName"),
    ],
    ids=[
        "normal_names",
        "another_normal_names",
        "empty_first_name",
        "empty_last_name",
        "both_names_empty",
        "single_name",
    ],
)
def test_concat_names_with_a_space(names, expected):
    assert concat_names_with_a_space(names) == expected
    