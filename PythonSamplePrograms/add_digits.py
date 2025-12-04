def add_digits(num: int)->int:

    while num > 9:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        num = sum
    return num


print(add_digits(38))
print(add_digits(0))
