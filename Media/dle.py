x = range(2,10)

print(next(iter(x)))
print(next(iter(x)))
b = iter(x)
print(b.__next__())
print(b.__next__())

