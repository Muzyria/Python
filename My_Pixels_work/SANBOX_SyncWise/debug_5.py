import math

# Параметры задачи
start_capital = 1000  # начальный капитал
target_amount = 100000  # конечная сумма
daily_growth_rate = 0.5  # ежедневный рост (20%)

# Вычисление количества дней
n = math.log(target_amount / start_capital) / math.log(1 + daily_growth_rate)

print(f"Количество дней: {math.ceil(n)}")
