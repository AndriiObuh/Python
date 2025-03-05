# Ось декоратор, який імітує авторизацію користувача. Він перевіряє, чи має користувач доступ перед виконанням функції:

def auth_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin", False):  # Перевіряємо, чи user має is_admin=True
            print(f"Доступ заборонено для {user['name']}")
            return None
        print(f"Доступ дозволено для {user['name']}")
        return func(user, *args, **kwargs)
    
    return wrapper

@auth_required
def delete_data(user):
    print("Дані успішно видалено!")

# Тестуємо декоратор
admin = {"name": "Andrii", "is_admin": True}
guest = {"name": "Oleh", "is_admin": False}

delete_data(admin)  # ✅ Доступ дозволено
delete_data(guest)  # ❌ Доступ заборонено
# 📌 Вивід:
# Доступ дозволено для Andrii
# Дані успішно видалено!
# Доступ заборонено для Oleh
# 🔍 Як це працює?
# Функція auth_required перевіряє, чи є у словнику user ключ "is_admin" зі значенням True.
# Якщо користувач не адміністратор, виводиться повідомлення "Доступ заборонено", і функція не виконується.
# Якщо адміністратор, функція виконується нормально.
# ✅ Тепер можна легко додавати перевірку прав доступу до будь-якої функції!