# Напиши функцію, яка приймає рядок, перетворює його в список чисел (розділених пробілами) і повертає їх суму.
# Приклад
# numbers = "1 2 3 4 5"

# Ось функція, яка приймає рядок, перетворює його в список чисел і повертає їхню суму:

def sum_of_numbers(numbers_str):
    try:
        # Розбиваємо рядок на окремі елементи та перетворюємо їх у числа
        numbers_list = [int(num) for num in numbers_str.split()]
        return sum(numbers_list)
    except ValueError:
        raise ValueError("Рядок має містити лише цілі числа, розділені пробілами.")

# Приклад використання
numbers = "1 2 3 4 5"
result = sum_of_numbers(numbers)
print(result)  # 15
# Що робить ця функція?
# Розбиває рядок за пробілами:

# numbers_str.split()
# "1 2 3 4 5" → ["1", "2", "3", "4", "5"]

# Перетворює кожен елемент у число за допомогою list comprehension:


# [int(num) for num in numbers_str.split()]
# ["1", "2", "3", "4", "5"] → [1, 2, 3, 4, 5]

# Обчислює суму всіх чисел:

# sum(numbers_list)
# Обробка помилок:
# Якщо у рядку є символи, які не можна перетворити в число, викличеться помилка ValueError.

# Приклади використання

print(sum_of_numbers("10 20 30"))  # 60
print(sum_of_numbers("5 5 5 5"))   # 20
print(sum_of_numbers("100 200 300 400"))  # 1000
# ❌ Помилковий ввід:

print(sum_of_numbers("1 2 три 4 5"))  # ValueError: Рядок має містити лише цілі числа, розділені пробілами.
# Розширена версія (з підтримкою десяткових чисел)
# Якщо потрібно підтримувати числа з плаваючою точкою, змінюємо int(num) на float(num):

def sum_of_numbers(numbers_str):
    try:
        numbers_list = [float(num) for num in numbers_str.split()]
        return sum(numbers_list)
    except ValueError:
        raise ValueError("Рядок має містити лише числа, розділені пробілами.")

# Приклад
print(sum_of_numbers("1.5 2.5 3.5"))  # 7.5