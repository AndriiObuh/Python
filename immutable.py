a = (1, 2, 3)
b = a  # b посилається на той самий кортеж, що й a
a = (10, 2, 3)  # Створюється новий кортеж, і a тепер посилається на новий
print(b)
# print(a)

list1 = [1, 2, 3]
list2 = list1.copy()  # Тепер list2 — це копія list1
list1.append(4)
print(list2)  # Виведе: [1, 2, 3], list2 не зміниться
print(list1)

x = 10
print(id(x))  # ID першого об'єкта

x += 5
print(id(x))

s = "hello"
print(id(s))

s += " world"
print(id(s))  # Новий об'єкт, оскільки рядки незмінні

lst = [1, 2, 3]
print(id(lst))  # ID початкового списку

lst.append(4)
print(id(lst))  # ID не змінився