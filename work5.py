# import datetime
# m, d = [2,  28]
#
# m, d = 2022
#
# s = 'я учу питон'
# ch = 'о'
# for i in s:
#     if i != '':
#         print(i, end='')

# m,  n = 54, 9184
# for i in range(m, n+1):
#     if i % 5 == 0:
#         print(i, end=' ')

# mas = ['a', 1, True, 'pithon']
# for i in mas:
#     print(type(i))
#
# ar = ['a', 1, True, 'pithon']
# ar2 = list()
# print(ar.count(1))
# ar.reverse(1))
# масивы
# arr  = [32]
# arr_ = []

#
#  s = 'Москва Астрахань Новгород Димитровград Душанбе'
#  s = s.lower().replase('ь', '').replase('ь', '').replase('ы', '')
#  print(s)
#  arr = s.split()
#  print(arr)
#  num = 0
#  for i in range(len(arr) - 1)
#      if arr[i][-1] == arr[i+1][0]:
#          num +- 1
#
# if num == len(arr):

# num = 6
# count = 0
# for i in range(2, num):
#     if num % i == 0:
#         count += 1
#
# # print('Да' if count == 0  else 'Нет')
# s = '10'+25-12''
# s = s.replace('- ', '- ').replace('+ ', '').replace(' ', ' ')
#
# arr = list(map(int, s.split()))
#
# num = 11
# list_nums = []
# for i in range(2, num):
#     for j in range(2, i+1):
#         if i % j  == 0:
#             break
#         else:
#             list_nums.append(i)
# print(*list_nums)
#
# list_ = []
# for i in range(5):
#     list_2 = []
#     for j in range

# Генератор
# gen_1 = (i for i in range(100000))
# gen_2 = (i for i in range(100000))
#
# import sys
# print(sys.getsizeof(gen_2))


#
# i = 0
# while i < 10:
#     i += 1
# i -= 10
# print(i)
# lst_2 = [j for j in range(50) if j  % 2 == 0]
# print(lst_2)
#
# list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
# list_b = [x**2 if x%2 == 0 else x**3 for x in list_a if x>0]
# print(list_b)



# i = str(input())
# while i < 10:
#     i += 1
# i -= 10
# print(i)
# lst_2 = [j for j in range(50) if j  % 2 == 0]
# print(lst_2)