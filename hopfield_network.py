import numpy as np

# Функция активации Хопфилда
def activation(x):
    return np.where(x >= 0, 1, -1)

# Создание данных поврежденных цифр
damaged_digits = np.zeros((10, 5, 5))

# Создание повреждений на изображениях цифр
for i in range(10):
    digit = np.array([
        [-1, -1, -1, -1, -1],
        [-1,  1,  1,  1, -1],
        [-1,  1, -1,  1, -1],
        [-1,  1,  1,  1, -1],
        [-1, -1, -1, -1, -1]
    ])
    indices = np.random.choice(25, size=7, replace=False)
    digit[indices // 5, indices % 5] = -1
    damaged_digits[i] = digit

# Создание вектора весов Хопфилда
weights = np.zeros((25, 25))
for digit in damaged_digits:
    flattened_digit = digit.flatten()
    weights += np.outer(flattened_digit, flattened_digit)

# Итерация по поврежденным цифрам для восстановления
for i, damaged_digit in enumerate(damaged_digits):
    flattened_damaged_digit = damaged_digit.flatten()
    for j in range(10):
        # Применение функции активации Хопфилда
        result = activation(np.dot(weights, flattened_damaged_digit))
        # Преобразование результата к матричному виду
        result_matrix = np.reshape(result, (5, 5))
        # Вывод результата
        print(f"Recovered digit {i}:")
        print(result_matrix)
        print()