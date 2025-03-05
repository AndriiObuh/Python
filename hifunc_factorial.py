# 🔹 5. Факторіал (рекурсія)
# Напиши рекурсивну функцію для знаходження факторіалу n!.

# 🔹 Варіант 1: Рекурсія

def factorial(n):
    if n == 0 or n == 1:  # Базовий випадок
        return 1
    return n * factorial(n - 1)  # Рекурсивний виклик

# Перевірка
print(factorial(5))  # 120
print(factorial(3))  # 6
print(factorial(0))  # 1
print(factorial(7))  # 5040
# ✔️ Як це працює?

# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 (базовий випадок)

# 🔹 Варіант 2: Через цикл for (ітеративний метод)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Перевірка
print(factorial(5))  # 120
# ✔️ Цей метод працює швидше, ніж рекурсія, бо немає зайвих викликів функцій.

# 🔹 Варіант 3: Використання math.factorial

import math

print(math.factorial(5))  # 120
# ✔️ Найшвидший спосіб, якщо можна використовувати вбудовані функції.
