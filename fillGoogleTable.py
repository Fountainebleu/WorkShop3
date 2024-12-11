import gspread
import pandas as pd


# Данные для уровней сложности
data = {
    "Level": list(range(1, 11)),
    "Speed": [4, 6, 8, 10, 12, 14, 16, 18, 20, 22],
    "TimeBetweenEggDrops": [1.5, 1.4, 1.3, 1.2, 1.1, 1, 0.9, 0.8, 0.7, 0.6],
    "ChanceDirection": [0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055],
    "LeftRightDistance": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
}

# Создаем DataFrame
df = pd.DataFrame(data)

gc = gspread.service_account(filename='workshop3-444213-54e81ec1546f.json')
sh = gc.open("WorkShop3")

# Формируем список данных для записи
values = df.values.tolist()

# Обновляем диапазон данных за один раз
sh.sheet1.update('A2:E11', values)