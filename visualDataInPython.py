import pandas as pd
import matplotlib.pyplot as plt

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

# Визуализация данных
plt.figure(figsize=(12, 8))

# Скорость
plt.subplot(2, 2, 1)
plt.plot(df["Level"], df["Speed"], marker='o', label="Speed", color='blue')
plt.title("Dragon Speed by Level")
plt.xlabel("Level")
plt.ylabel("Speed")
plt.grid(True)

# Время между сбросами
plt.subplot(2, 2, 2)
plt.plot(df["Level"], df["TimeBetweenEggDrops"], marker='o', label="Time Between Egg Drops", color='red')
plt.title("Time Between Egg Drops by Level")
plt.xlabel("Level")
plt.ylabel("Time (seconds)")
plt.grid(True)

# Шанс смены направления
plt.subplot(2, 2, 3)
plt.plot(df["Level"], df["ChanceDirection"], marker='o', label="Chance Direction", color='green')
plt.title("Chance of Changing Direction by Level")
plt.xlabel("Level")
plt.ylabel("Chance")
plt.grid(True)

# Дистанция движения
plt.subplot(2, 2, 4)
plt.plot(df["Level"], df["LeftRightDistance"], marker='o', label="Left Right Distance", color='purple')
plt.title("Left-Right Distance by Level")
plt.xlabel("Level")
plt.ylabel("Distance")
plt.grid(True)

plt.tight_layout()
plt.show()