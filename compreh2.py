# 2️⃣ Використовуючи Dict Comprehension, створи словник, де ключі – це числа від 1 до 5, а значення – їх факторіали.
from math import factorial

# dct = {i: i.factorial() for i in range(1, 6)}
# print(dct)

# Майже правильно! Але є маленька помилка в коді. Метод .factorial() є функцією з бібліотеки math, а не методом для інтерger-типів. Тому правильний код буде виглядати так:

from math import factorial

dct = {i: factorial(i) for i in range(1, 6)}
print(dct)
# Цей код створює словник, де ключі — це числа від 1 до 5, а значення — це їх факторіали. Результат буде таким:

# {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
# Це правильний словник, де ключі відповідають числам від 1 до 5, а значення — це їх факторіали:
