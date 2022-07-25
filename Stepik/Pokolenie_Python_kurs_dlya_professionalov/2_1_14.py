
def get_biggest(numbers):
    if numbers:
        str_numbers = [str(i) for i in numbers]
        for i in range(len(numbers)):
            index = i
            for j in range(i + 1, len(numbers)):
                if str_numbers[j] + str_numbers[index] > str_numbers[index] + str_numbers[j]:
                    index = j
            str_numbers[i], str_numbers[index] = str_numbers[index], str_numbers[i]
        return int(''.join(str_numbers))
    return -1



print(get_biggest([1, 2, 3])) # 3 2 1
print(get_biggest([61, 228, 9, 3, 11])) # 9 61 3 228 11
print(get_biggest([7, 71, 72])) # 7 72 71
print(get_biggest([])) # -1