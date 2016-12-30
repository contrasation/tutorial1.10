# a = [66.25, 333, 333, 1, 1234.5]
# print a.count(333), a.count(66.25), a.count('x')
#
# a.insert(2, -1)
# a.append(333)
# print a
#
# print a.index(333)
#
# a.remove(333)
# print a
#
# a.reverse()
# print a
#
# a.sort()
# print a
#
# print a.pop()
# print a

# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print stack
# print stack.pop()
# print stack.pop()
# print stack

# from collections import deque
# queue = deque(['Eric', 'Jhon', 'Michael'])
# queue.append('Terry')
# queue.append('Graham')
# print queue
# print queue.popleft()
# print queue

# def f(x):
#     return x % 3 == 0 or x % 5 == 0
#
# a = [x for x in range(1, 10)]
# b = [y for y in range(30, 50)]
# c = a + b
# print c
# # print filter(f, range(2, 25))
# print filter(f, c)

# def cube(x):
#     return x*x*x
#
# print map(cube, range(1, 11))

# seq = range(8)
# seq2 = range(10,18)
# def add(x, y):
#     return x + y
#
# print map(add, seq, seq2)

# def add(x, y):
#     return x + y
#
# print reduce(add, range(1,11))

# def sum(seq):
#     def add(x, y):
#         return x + y
#     return reduce(add, seq, 0)
#
# print sum(range(1, 11))
# print sum([])

# squares = []
# for x in range(10):
#     squares.append(x**2)
#
# print squares

# squares = [x**2 for x in range(10)]
# print squares

# squares = map(lambda x: x**2, range(10))
# print squares

# print [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# vec = [-4, -2, 0, 2, 4]
# print [x*2 for x in vec]
#
# print [x for x in vec if x >= 0]
#
# print [abs(x) for x in vec]
#
# freshfruit = ['  banana', '  loganberry', 'passion fruit  ']
# print [weapon.strip() for weapon in freshfruit]
#
# print [(x, x**2) for x in range(6)]
#
# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print [num for elem in vec for num in elem]
#
# from math import pi
# print [str(round(pi, i)) for i in range(1,10)]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# print [row for row in matrix]
# print [[row[i] for row in matrix] for i in range(4)]
#
# # def func(matrix):
# #     for row in matrix:
# #         for i in range(4):
# #             print row[i]
# #
# # print func(matrix)
#
# trans = []
# for i in range(4):
#     trans.append([row[i] for row in matrix])
#
# print trans
#
#
# trans = []
# for i in range(4):
#     trans_row = []
#     for row in matrix:
#         trans_row.append(row[i])
#     trans.append(trans_row)
#
# print trans

print zip(*matrix)
