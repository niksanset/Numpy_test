import numpy as np

sales_data = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600]
# Среднее значение

mean = np.mean(sales_data)
print("Среднее значение продаж:", mean)

# Средневзвешенное значение
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

weighted_mean = np.average(sales_data, weights=weights)
print("Средневзвешенное значение продаж:", weighted_mean)

# Максимальное значение

maximum = np.max(sales_data)
print("Максимальное значение продаж:", maximum)

# Минимальное значение

minimum = np.min(sales_data)
print("Минимальное значение продаж:", minimum)

# Дисперсия

variance = np.var(sales_data)
print("Дисперсия продаж:", variance)