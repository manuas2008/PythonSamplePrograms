from PythonSamplePrograms.power_of_2 import power_of_2

def test_input_64():
    assert power_of_2(64) == True

def test_input_218():
    assert power_of_2(218) == False

def test_input_2():
    assert power_of_2(2) == True