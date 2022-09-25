# generator
def gen(n):
    for i in range(n):
        yield i
# or 
def gen_():
    yield 1
    # pause
    yield 2
    # pause 
    yield 3
x = gen(3)
print(x.__next__())
print(x.__next__())
print(x.__next__())

# this is how iterATOR WORK
# class A:
#     def __init__(self,n):
#         self.n = n
#     def __iter__(self):
#         self.x = 0
#         return self
#     def __next__(self):
#         self.x += 1
#         if self.x > self.n:
#             raise StopIteration
#         return self.x
# itr = A(20)
# print(iter(itr).__next__())


# class A:
#     def __init__(self):
#         self.x = 120
#     def disp(self):
#         print('value of x is '+str(self.x))

# with A as b:
#     b.disp()