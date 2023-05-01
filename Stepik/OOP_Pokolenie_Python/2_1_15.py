
def intersperse(iterable, delimiter):

    def my_iter():
        iterator = iter(iterable)
        yield next(iterator)
        for item in iterator:

            yield item


    new_list = [next(item) if i % 2 == 0 else delimiter for i in range(len(list(iterable)) * 2 - 1)]
    return new_list


# print(*intersperse([1, 2, 3], 0))
# print(*intersperse('beegeek', '!'))
# print(*intersperse('A', '...'))

iterable = iter('Beegeek')
print(*intersperse(iterable, '+'))