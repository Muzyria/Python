def print_operation_table(operation, rows, cols):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print(operation(i, j), end=' ')
        print()


print_operation_table(lambda a, b: a * b, 5, 5)
