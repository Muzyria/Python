
def index_of_nearest(numbers, number):
    if numbers:
        data = [abs(i- number) for i in numbers]
        return data.index(min(data))    
    return -1


print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))
