import sys

def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

dir(sys)
print("Integers: From %d to %d\n" %  (-sys.maxsize - 1, sys.maxsize))
print("Floating point: Positive nonzeros From %.25g to %.25g\n" % (sys.float_info.min, sys.float_info.max))
print("Floating point: Positive nonzeros From %g to %g\n" % (sys.float_info.min, sys.float_info.max))
print(fac(100))
