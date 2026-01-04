from PythonSamplePrograms.equilibrium_point import findEquilibrium


def test_equilibrium_point_at_middle():
    """Test case where equilibrium point exists in the middle"""
    assert findEquilibrium([1, 3, 5, 2, 2]) == 2


def test_equilibrium_point_single_element():
    """Test case with single element - no middle element to check"""
    assert findEquilibrium([5]) == -1


def test_equilibrium_point_two_elements():
    """Test case with two elements - no middle element to check"""
    assert findEquilibrium([1, 2]) == -1


def test_no_equilibrium_point():
    """Test case where no equilibrium point exists"""
    assert findEquilibrium([1, 2, 3, 4, 5]) == -1


def test_equilibrium_point_with_negative_numbers():
    """Test case with negative numbers"""
    assert findEquilibrium([1, -1, 3, -2, 2]) == 2


def test_equilibrium_point_with_zeros():
    """Test case with zeros"""
    assert findEquilibrium([0, 0, 0]) == 1


def test_equilibrium_point_larger_array():
    """Test case with larger array"""
    assert findEquilibrium([1, 2, 3, 4, 5, 3, 2, 1]) == -1


def test_equilibrium_point_first_valid_position():
    """Test case where equilibrium is at first valid position"""
    assert findEquilibrium([3, 0, 0, 0, 0]) == -1


def test_all_same_elements():
    """Test case where all elements are the same"""
    arr = [2, 2, 2, 2, 2]
    result = findEquilibrium(arr)
    # For [2, 2, 2, 2, 2], index 2 has left_sum=4, right_sum=4
    assert result == 2


def test_large_numbers():
    """Test case with large numbers"""
    assert findEquilibrium([1000000, 1000, 1, 1000, 1000000]) == 2
