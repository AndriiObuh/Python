# 🔹 9. Перевірка анаграми
# Напиши функцію, яка перевіряє, чи є два слова анаграмами (мають однакові букви, але в іншому порядку).
# 📌 Приклад:
# print(is_anagram("listen", "silent"))  # True
# print(is_anagram("hello", "world"))    # False

# 🔹 Спосіб 1: Використання sorted()
# 📌 Ідея: Якщо відсортувати букви у двох словах, вони будуть однаковими для анаграм.

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

# 🔹 Перевірка
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
print(is_anagram("evil", "vile"))      # True
# ✅ Плюси: Простий, зрозумілий, швидко працює для коротких слів.
# ❌ Мінуси: Сортування має складність O(n log n), тому повільне для довгих слів.

# 🔹 Спосіб 2: Використання Counter (ефективніший спосіб)
# 📌 Ідея: Підраховуємо, скільки разів кожна літера зустрічається в обох словах.

from collections import Counter

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

# 🔹 Перевірка
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
print(is_anagram("evil", "vile"))      # True
# ✅ Плюси: Працює за O(n), ефективніший за сортування.
# ❌ Мінуси: Використовує більше пам’яті (створює два Counter).

# 🔹 Додатково: Ігноруємо регістр та пробіли
# 📌 Проблема: "Listen" і "Silent" — анаграми, але sorted("Listen") != sorted("Silent").
# 📌 Рішення: Перетворюємо на нижній регістр та видаляємо пробіли.

def is_anagram(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return Counter(word1) == Counter(word2)

# 🔹 Перевірка
print(is_anagram("Listen", "Silent"))      # True
print(is_anagram("Astronomer", "Moon starer"))  # True
print(is_anagram("Hello", "world"))        # False
# ✅ Плюси: Коректно обробляє регістр і пробіли.