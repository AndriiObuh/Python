# 1️⃣ Використовуючи List Comprehension, створи список, що містить квадрати чисел від 1 до 10, які діляться на 3.

lst = [i ** 2 for i in range(1, 11) if i % 3 == 0]

print(lst)