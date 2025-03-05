# Напиши функцію, яка приймає рядок і повертає кількість голосних літер (a, e, i, o, u).

# def count_vowels(s):
#     pass  # Твій код тут

# # Перевірка
# print(count_vowels("hello"))  # 2
# print(count_vowels("programming"))  # 3

def count_vowels(s):
    vowels = "aeiouAEIOU"  # Враховуємо як маленькі, так і великі голосні
    count = sum(1 for char in s if char in vowels)  # Підраховуємо голосні
    return count

# Перевірка
print(count_vowels("hello"))  # 2
print(count_vowels("programming"))  # 3
print(count_vowels("AEIOU"))  # 5
print(count_vowels("bcdfg"))  # 0
# 🔍 Як це працює?
# Створюємо рядок vowels, що містить усі голосні (a, e, i, o, u) у верхньому та нижньому регістрах.
# Використовуємо генератор виразів sum(1 for char in s if char in vowels), який перебирає кожен символ у s і додає 1, якщо символ є голосною.
# Цей метод ефективний і працює за O(n), де n — довжина рядка.
    