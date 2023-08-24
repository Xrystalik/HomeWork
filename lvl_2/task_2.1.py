# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
#* [42, 54, 65, 87, 0]             -> min = 0, max = 87
#* [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

def maximum(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

def minimum(lst):
    min_num = lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
    return min_num

# Примеры использования функций

lst1 = [5, 9, 25, 135, 987, 633, -34, 56]
print("max =", maximum(lst1), ", min =", minimum(lst1))

lst2 = [-524, 516, 10, 24, -34, 0, -130]
print("min =", minimum(lst2), ", max =", maximum(lst2))

lst3 = [12, 154, 35, 57, 0]
print("min =", minimum(lst3), ", max =", maximum(lst3))

lst4 = [5, 120, 34, 56, -26, 87]
print("min =", minimum(lst4), ", max =", maximum(lst4))