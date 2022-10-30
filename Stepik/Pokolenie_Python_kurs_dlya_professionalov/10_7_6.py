# def parse_ranges(ranges):
#     gen1 = (list(map(int, i.split('-'))) for i in list(map(str, ranges.split(','))))
#     return (j for i in gen1 for j in range(i[0], i[1] + 1))
def parse_ranges(ranges: str):
    for r in ranges.split(","):
        start, end = map(int, r.split("-"))
        yield from range(start, end+1)


print(*parse_ranges('1-2,4-4,8-10'))

print(*parse_ranges('1-10,2-10'))

print(*parse_ranges('7-32'))
