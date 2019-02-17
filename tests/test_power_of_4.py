from PythonSamplePrograms.power_of_4 import power_of_4

def test_power_of_4_input_64():
    assert power_of_4(64) == True

def test_power_of_4_input_5():
    assert power_of_4(5) == False