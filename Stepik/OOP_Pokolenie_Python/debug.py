
my_list = [1, 2, 3, 4, 5]
new_list = [(lambda x: x * ()-1 if x % 2 else x * 1 )(num) for num in my_list]
print(new_list)