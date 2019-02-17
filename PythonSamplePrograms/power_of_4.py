def power_of_4(num):
    bin_val = 0b01010101010101010101010101010100
    if num < 0:
        return False
    elif num == 1:
        return True

    if bin(num).count('1') == 1 and num & bin_val == num:
        return True
    else:
        return False

print(power_of_4(64))