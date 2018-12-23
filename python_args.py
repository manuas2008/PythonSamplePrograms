def adder(*args):
    sum = 0
    for n in args:
        sum+=n
    print("Sum = {}".format(sum))
    return sum

adder(1,2,3,4,5)
adder(1,200,344)