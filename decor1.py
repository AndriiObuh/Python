# Створи декоратор, який підраховує, скільки разів була викликана функція.
# Ось декоратор, який підраховує кількість викликів функції та виводить її назву разом із кількістю викликів:

def call_counter(func):
    count = 0  # Лічильник викликів
    
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функція {func.__name__} викликана {count} раз(и)")
        return func(*args, **kwargs)
    
    return wrapper

@call_counter
def say_hello():
    print("Hello, world!")

@call_counter
def add(a, b):
    return a + b

# Тестуємо декоратор
say_hello()
say_hello()
print(add(2, 3))
print(add(10, 5))
# 📌 Вивід:
# Функція say_hello викликана 1 раз(и)
# Hello, world!
# Функція say_hello викликана 2 раз(и)
# Hello, world!
# Функція add викликана 1 раз(и)
# 5
# Функція add викликана 2 раз(и)
# 15
# 🔍 Як це працює?
# Ми створюємо змінну count, яка зберігає кількість викликів функції.
# Використовуємо nonlocal count, щоб змінювати змінну count в wrapper().
# Перед кожним викликом функції збільшуємо лічильник і виводимо його значення.
# Викликаємо оригінальну функцію func(*args, **kwargs).
# ✅ Тепер кожен виклик функції буде підраховуватись!