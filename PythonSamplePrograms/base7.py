def convertToBase7(num: int) -> int:
    base7 = 0
    ten_pow = 0
    while num >= 7:
        base7 += 10 ** ten_pow * (num % 7)
        num //= 7
        ten_pow += 1
    base7 += 10 ** ten_pow * num
    return base7

print(convertToBase7(10))
print(convertToBase7(72))
print(convertToBase7(-10))