# Напиши функцію, яка приймає список чисел і повертає суму всіх парних чисел.

def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Приклад використання
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(nums)
print(result)  # Виведе: 30
# Пояснення коду:
# Використовується генератор виразів для відбору тільки парних чисел:

# (num for num in numbers if num % 2 == 0)
# Функція sum() підсумовує всі парні числа.