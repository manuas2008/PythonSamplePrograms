from PythonSamplePrograms.two_sum import Solution

def test_two_sum_positive():
    s = Solution()
    assert (s.twoSum([2, 7, 11, 15], 9) == [0, 1])

def test_two_sum_negative():
    s = Solution()
    assert (s.twoSum([2, 7, 11, 15], 8) == None)


