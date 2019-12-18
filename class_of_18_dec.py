from functools import reduce


a_list = [2, 3, 4, 5, 10, 8, 3, 4, 6, 23, 0]


# def my_square(list_):
#     new_list = []
#     for i in list_:
#         new_list.append(i ** 2)
#     return new_list
#
#
# print(my_square(a_list))
# print(list(map(lambda x: x ** 2, a_list)))
#
# a_new_list = []
# for x in a_list:
#     a_new_list.append(x ** 2)
# print([x ** 2 for x in a_list])
#
#
# def my_square_map(item):
#     return item ** 2
#
#
# # print(list(map(my_square_map, a_list)))
# print(list(map(my_square_map, a_list)))
#
#
# new_list = list(map(str, a_list))
# print(new_list)
# print(type(a_list[0]))
# print(type(new_list[0]))
#
# new_list_ = []
# for i in a_list:
#     new_list_.append(str(i))
# print(type(new_list_[0]))


print(list(filter(lambda x: x <= 4, a_list)))
print([x for x in a_list if x <= 4])

print(a_list)
a_str = ['Salman', 'Abd', 'Rihab', '', 'Kabir', []]
print(list(filter(None, a_str)))


print(reduce(lambda x, y: x*y, list(filter(None, a_list))))
mul = 1
for i in a_list:
    if i:
        mul = mul * i
print(mul)
print([mul * i for i in a_list if i])

