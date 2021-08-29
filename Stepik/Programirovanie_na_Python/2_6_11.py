size = int(input())
table = [[0 for i in range(size)] for i in range(size)]
all_count_elem = size ** 2
corr_count_elem = 0
shift_row = 0
shift_col = 0
while corr_count_elem < all_count_elem:
    for i in range(shift_row,size):
        corr_count_elem += 1
        table[shift_row][i] = corr_count_elem
    for i in range(shift_row + 1,size):
        corr_count_elem += 1
        table[i][size - 1] = corr_count_elem
    for i in range(size - 2, shift_col - 1, -1):
        corr_count_elem += 1
        table[size - 1][i] = corr_count_elem
    for i in range(size - 2,shift_row ,-1):
        corr_count_elem += 1
        table[i][shift_col] = corr_count_elem
    size -= 1
    shift_row += 1
    shift_col += 1
for i in range(len(table)):
    print(*table[i])