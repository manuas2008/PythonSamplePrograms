######### Generate Fibonacci Sequence #########
# a, b = 0, 1
# for i in range(0, 10):
#     print("fib[{}]:{}".format(i+1, a))
#     a, b = b, a+b

######### Generate Fibonacci Sequence using Function #########
def genFibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        print("fib[{}]:{}".format(i + 1, a))
        a, b = b, a+b

genFibonacci(10)