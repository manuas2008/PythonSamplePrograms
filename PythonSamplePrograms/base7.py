def convertToBase7(num: int) -> int:
    negative = 1
    if num < 0:
        negative = -1
        num = abs(num)
    base7 = 0
    ten_pow = 0
    while num >= 7:
        base7 += 10 ** ten_pow * (num % 7)
        num //= 7
        ten_pow += 1
    base7 += 10 ** ten_pow * num
    return base7 * negative

print(convertToBase7(10))
print(convertToBase7(72))
print(convertToBase7(-10))