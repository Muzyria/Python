def is_valid(value):
    return 4 <= len(value) <= 6 and value.isdigit()
        

print(is_valid('4367'))
print(is_valid('92134'))
print(is_valid('89abc1'))
print(is_valid('900876'))
print(is_valid('49 83'))
