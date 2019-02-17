def add_n(n):
    print('INSIDE ADD_N() - N={}'.format(n))
    return lambda x: x+n

add_3 = add_n(3)
add_4 = add_n(4)

print(add_3(10))
print(add_4(10))

