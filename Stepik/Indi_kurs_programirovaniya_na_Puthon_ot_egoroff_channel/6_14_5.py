print((True, False)[bool(sum([int(v) if i % 2 == 0 else (lambda x: x * 2 if x * 2 < 10 else x * 2 - 9)(int(v)) for i, v in enumerate(input(), 1)]) % 10)])
