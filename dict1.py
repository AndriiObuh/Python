# 1️⃣ Функція name_lengths(lst), яка приймає список імен та повертає словник, де ключ – ім'я, а значення – його довжина.
# print(name_lengths(["Alice", "Bob", "Charlie"]))  
# # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

def name_lengths(lst):
    return {name: len(name) for name in lst}

print(name_lengths(["Alice", "Bob", "Charlie"]))  
# {'Alice': 5, 'Bob': 3, 'Charlie': 7}
# 🔍 Пояснення коду:
# Використовуємо словникове включення (dict comprehension), щоб створити словник.
# name: len(name) – ключем буде ім'я, а значенням – його довжина.
# Функція працює для будь-якого списку імен.