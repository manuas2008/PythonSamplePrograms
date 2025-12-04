from PythonSamplePrograms.three_sum import three_sum

def test_three_sum_positive():
    assert (three_sum([-1,0,1,2,-1,-4]) == [[-1, -1, 2], [-1, 0, 1]])

def test_two_sum_negative():
    assert(three_sum([1,2,3]), [])
