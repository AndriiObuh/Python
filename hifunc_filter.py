# 🔹 3. Фільтрація парних чисел
# Напиши функцію, яка приймає список чисел і повертає тільки парні числа.

# ✅ Варіант 1: За допомогою циклу for

def filter_even(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    return even

print(filter_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
print(filter_even([10, 15, 20, 25]))  # [10, 20]

# ✅ Варіант 2: Використання list comprehension (спискового включення)

def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# Перевірка
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
# Цей варіант коротший та ефективніший.

# ✅ Варіант 3: Використання filter()

def filter_even_numbers(lst):
    return list(filter(lambda num: num % 2 == 0, lst))

# Перевірка
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
# Функція filter() проходить по списку та залишає тільки ті елементи, для яких lambda num: num % 2 == 0 повертає True.

# 🏆 Що вибрати?
# Цикл for — зрозумілий та гнучкий, можна додати додаткову логіку.
# Спискове включення (list comprehension) — найоптимальніший спосіб.
# filter() — працює трохи повільніше, але більш декларативний стиль.