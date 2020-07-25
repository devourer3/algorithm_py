import sys

a = range(10000)
b = [n for n in range(10000)]

print(sys.getsizeof(a))
print(sys.getsizeof(b))