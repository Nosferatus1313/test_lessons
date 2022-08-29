# Открытие файла
import os
# f = open('text_file1.txt', 'r',  encoding='utf-8')
# print(*f)

# p = os.getcwd()
# f = open(p + 'r',  encoding='utf-8')
# print(*f)

# p = os.getcwd()
# f = open('../PycharmProject/some_file.text, 'r'  encoding='utf-8')
# print(*f)

# Закрытие файла
# p = os.getcwd()
# f = open(p + 'r',  encoding='utf-8')
# f.write('phyton')
# f.close()

# try:
#     f = open('text_file1.text', 'r', encoding='utf-8')
#     f.write('phyton')
# except:
#     print()
# finally:
#     print ()
#     f.close()

# with open('text_file1.txt', 'r',  encoding='utf-8') as f:
#     print(*f)

# while True
# with open('users_file.txt', 'a+',  encoding='utf-8') as f:
#     while True:
#         s = input()
#         if s | = '':
#             f.write(s + '\n)'
#         else:
# break
#
# матрицы

import random
# lst = [i**3 if i < 50 else i**2 for i in range(100) if i % 3 == 0 and i % 5 == 0]
# print(lst)

# lst = [(0) * 5 for _ in range(4)]
# lst[]
#     lst.append([0] * 2)
# for line in lst:
#     print(*line)
#
#  lst = [[0, 1, 2, True],
#        [{}, 11, ['a', 'b', 'c'], 13],
#        [20, 25]]
#  for line in lst:
#     print(*line)

# w, h = 5, 3
# matrix = [[0 for x in range(w) for y in range(h)]]
# print(matrix)
#
# lst1 = []
# for x in range(h):
#     lst2 = []
#     for y in range(w)

# w, h = 5, 3
# matrix = [[0 for x in range(w) for y in range(h)]]
# print(matrix)
# matrix[2][2] = 1
# for line in matrix:
#     print(*line)

# sum = 0
# n = int(input())
# while n != 0:
#     sum += n
#     n  = int(input())
# print(sum)

# a = (map(float, ['4.35', '-10.6', '1.0',  '200.34',  '0.56'])
# print(next(a))

numbers_1 = (1, 2, 3)
numbers_2 = (6,)
numbers_3 = (7, 8, 9, 10, 11, 12, 13)

s = numbers_1 * 2 + numbers_2 * 9 + numbers_3
list(s)
print(s)
