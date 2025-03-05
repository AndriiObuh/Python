# 1️⃣ Напиши функцію find_max(lst), яка знаходить найбільший елемент у списку.
# 2️⃣ Напиши функцію filter_even(lst), яка повертає список тільки з парними числами.
# 📌 Приклад:
# print(find_max([3, 7, 2, 8, 10, 4]))  # 10
# print(filter_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]

def find_max(lst):
    for i in lst:
      return max(lst)

print(find_max([3, 7, 2, 8, 10, 4]))


# def filter_even(lst):
#     for i in lst:
#         if i % 2 == 0:
#           return i
        
        
# print(filter_even([1, 2, 3, 4, 5, 6]))

# Твоя функція зараз працює неправильно, тому що return i завершує виконання функції після знаходження першого парного числа. Нам потрібно повертати весь список парних чисел.

# Правильний варіант:

def filter_even(lst):
    return [i for i in lst if i % 2 == 0]

print(filter_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
# 📌 Як це працює?

# [i for i in lst if i % 2 == 0] – це спискове включення (list comprehension), яке створює новий список, додаючи тільки парні числа.