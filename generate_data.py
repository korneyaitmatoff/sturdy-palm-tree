import random

# Функция для генерации вероятности зависимости
def calculate_alcohol_forecast(age, gender, performance, stress, family_alcohol, classmates_relations):
    base_risk = 0
    # Чем старше возраст, тем выше вероятность
    base_risk += (age - 5) * 3

    # Гендерное влияние (например, мальчики могут быть подвержены чуть больше)
    if gender == "М":
        base_risk += 5

    # Высокая успеваемость снижает вероятность
    base_risk -= performance * 0.2

    # Высокий уровень стресса повышает вероятность
    base_risk += stress * 5

    # Наличие семейной истории алкоголизма сильно увеличивает риск
    if family_alcohol:
        base_risk += 15

    # Плохие отношения с одноклассниками увеличивают риск
    if not classmates_relations:
        base_risk += 10

    # Приведение к диапазону 0-100
    return min(max(int(base_risk), 0), 100)

# Генерация данных
data = []
for _ in range(100):  # Генерация 100 записей
    age = random.randint(5, 18)
    gender = random.choice(["М", "Ж"])
    performance = random.randint(0, 100)
    stress = random.randint(0, 10)
    family_alcohol = random.choice([True, False])
    classmates_relations = random.choice([True, False])
    alcohol_forecast = calculate_alcohol_forecast(age, gender, performance, stress, family_alcohol, classmates_relations)

    data.append((age, gender, performance, stress, family_alcohol, classmates_relations, alcohol_forecast))

# Генерация DML-скрипта
with open("insert_data.sql", "w", encoding="utf-8") as f:
    f.write("INSERT INTO students (age, gender, performance, stress, family_alcohol, classmates_relations, alcohol_forecast) VALUES\n")
    rows = [
        f"({d[0]}, '{d[1]}', {d[2]}, {d[3]}, {str(d[4]).upper()}, {str(d[5]).upper()}, {d[6]})"
        for d in data
    ]
    f.write(",\n".join(rows) + ";")