from datetime import date


print(min(date.fromisoformat(input()), date.fromisoformat(input())).strftime('%d-%m (%Y)'))
