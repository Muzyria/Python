# def same_parity(nums):
    # return [i for i in nums if i % 2 == nums[0] % 2]


def same_parity(numbers):
    if len(numbers) != 0:
        if numbers[0] % 2 == 0:
            data = [i for i in numbers if i % 2 == 0] 
        if numbers[0] % 2 == 1:
            data = [i for i in numbers if i % 2 == 1] 
        return data    
    return numbers


print(same_parity([6, 0, 67, -7, 10, -20]))
print(same_parity([]))
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))