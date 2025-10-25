# код з простими змінними str та int, списками list, наборами set та словниками dict
# Змінні str та int
name = "Петро"
age = 25
height = 175.5

 # Список (list)
fruits = ["яблуко", "банан", "апельсин", "груша"]
fruits.append("ківі")

 # Набір (set)
unique_numbers = {1, 2, 3, 4, 4, 5, 5}  # Дублікати автоматично видаляються

 # Словник (dict)
person = {
     "name": "Іван",
     "age": 30,
     "city": "Київ",
     "hobbies": ["футбол", "музика", "подорожі"]
 }

 # Виведення всіх даних
print("=== Прості змінні ===")
print(f"Ім'я: {name}")
print(f"Вік: {age}")
print(f"Зріст: {height}")

print("\n=== Список фруктів ===")
print(f"Всі фрукти: {fruits}")
print(f"Перший фрукт: {fruits[0]}")

print("\n=== Унікальні числа (set) ===")
print(f"Набір чисел: {unique_numbers}")

print("\n=== Інформація про людину (dict) ===")
for key, value in person.items():
     print(f"{key}: {value}")


# Виведення вбудованих констант
print("\n=== Вбудовані константи Python ===")
print(f"True (тип: {type(True)}): {True}")
print(f"None (тип: {type(None)}): {None}")
print(f"False (тип: {type(False)}): {False}")

 # Виведення зарезервованих слів
import keyword
print("\n=== Зарезервовані слова Python ===")
print("Список всіх зарезервованих слів:")
print(keyword.kwlist)

 # Виведення результатів роботи вбудованих функцій
print("\n=== Результати роботи вбудованих функцій ===")

 # Демонстрація функції len()
test_list = [1, 2, 3, 4, 5]
test_string = "Привіт, світ!"
print(f"len(): Довжина списку {test_list}: {len(test_list)}")
print(f"len(): Довжина рядка '{test_string}': {len(test_string)}")

 # Демонстрація функції abs()
negative_number = -42.5
print(f"abs(): Абсолютне значення числа {negative_number}: {abs(negative_number)}")

 # Демонстрація функції round()
float_number = 3.14159
print(f"round(): Округлення числа {float_number} до 2 знаків після коми: {round(float_number, 2)}")

 # Демонстрація роботи циклів
print("\n=== Демонстрація роботи циклів ===")

 # 1. for цикл з range
print("\n1. Цикл for з range:")
print("Виведення чисел від 1 до 5:")
for i in range(1, 6):
     print(f"Число: {i}")

 # 2. for цикл для ітерації по колекції
print("\n2. Цикл for для списку:")
seasons = ["Зима", "Весна", "Літо", "Осінь"]
for season in seasons:
     print(f"Пора року: {season}")

 # 3. (переписано) for цикл замість while
print("\n3. Цикл for (переписано замість while):")
sum_numbers = 0
for counter in range(1, 6):
    sum_numbers += counter
    print(f"Крок {counter}: сума = {sum_numbers}")
print(f"Кінцева сума чисел від 1 до 5: {sum_numbers}")

 # Розгалуження — приклад 1: перевірка парності та знаку числа
print("\n=== Розгалуження: Приклад 1 ===")
num = -3
if num > 0:
 	sign = "позитивне"
elif num < 0:
 	sign = "негативне"
else:
 	sign = "нуль"
parity = "парне" if num % 2 == 0 else "непарне"
print(f"Число {num} є {sign} та {parity}.")

 # Розгалуження — приклад 2: градація оцінок
print("\n=== Розгалуження: Приклад 2 ===")
score = 78
if score >= 90:
 	grade = "A"
elif score >= 75:
	grade = "B"
elif score >= 60:
 	grade = "C"
else:
 	grade = "F"
print(f"Оцінка для балів {score}: {grade}")

 # Приклад конструкції try -> except -> finally з навмисною помилкою
print("\n=== Приклад try/except/finally ===")
try:
 	print("Спроба поділити 10 на 0 (навімисна помилка)")
 	result = 10 / 0  # тут виникне ZeroDivisionError
 	print(f"Результат: {result}")
except ZeroDivisionError as e:
 	print("Піймано помилку ZeroDivisionError:", e)
except Exception as e:
 	print("Піймано іншу помилку:", e)
finally:
 	# Блок finally виконується завжди — тут можна закривати файли/ресурси
 	print("Блок finally: цей код виконається незалежно від помилок")

 # Приклади використання контекст-менеджера `with`
print("\n=== Приклад with: робота з файлом ===")
filename = "lab2_example.txt"
 # Записуємо у файл в межах контексту — файл автоматично закриється
with open(filename, "w", encoding="utf-8") as f:
 	f.write("Це приклад роботи контекст-менеджера with.\n")
print(f"Записано у файл {filename}")

 # Зчитуємо файл також через with
with open(filename, "r", encoding="utf-8") as f:
 	content = f.read()
print("Вміст файлу:")
print(content.strip())

from contextlib import contextmanager, suppress

@contextmanager
def my_context(name):
    """Простий приклад власного контекст-менеджера через decorator contextmanager."""
    print(f"Entering context: {name}")
    try:
        yield {"name": name}
    finally:
        print(f"Exiting context: {name}")

print("\n=== Приклад with: власний контекст-менеджер ===")
with my_context("demo") as ctx_res:
 	print("В середині with, ресурс:", ctx_res)

print("\n=== Приклад contextlib.suppress ===")
 # suppress дозволяє під час with ігнорувати певні винятки
with suppress(ValueError):
 	print("Піднімаємо ValueError всередині suppress — воно буде придушене")
 	raise ValueError("Навмисна помилка, яка буде придушена")
print("Після suppress — виконання продовжується")

 # =====================
 # Приклади Python lambda
 # =====================
 # Коротко: lambda — це невелика анонімна функція, яка може приймати аргументи
 # і повертає вираз. Вона зручна для коротких однорядкових функцій, особливо
 # коли потрібно передати функцію як параметр (наприклад, у map, filter, sorted).

print("\n=== Приклади lambda ===")

 # 1) Простий lambda: квадрат числа
square = lambda x: x * x
print(f"square(5) через lambda: {square(5)}")

 # 2) Lambda з map: подвоїти всі елементи списку
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(f"Оригінал: {nums}, подвійні значення через map+lambda: {doubled}")

 # 3) Lambda як ключ для сортування (сортування списку кортежів за другим елементом)
people = [("Іван", 30), ("Марія", 25), ("Олег", 35)]
sorted_by_age = sorted(people, key=lambda p: p[1])
print(f"Люди відсортовані за віком: {sorted_by_age}")

 # Нотатки/рекомендації:
 # - lambda підходять для простих коротких функцій.
 # - для складної логіки краще використовувати def з іменованою функцією,
 #   бо def читається легше і дозволяє додавати докстрінги/дебаг.

