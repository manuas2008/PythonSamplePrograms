from PythonSamplePrograms.add_digits import add_digits

def test_add_digits_positive():
    assert(add_digits(38) == 2)

def test_add_digits_negative():
    assert(add_digits(0) == 0)
