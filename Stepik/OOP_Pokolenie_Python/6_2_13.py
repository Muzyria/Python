

# тест 1
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(list(sequencezip))
print(tuple(sequencezip))

# ответ
# [('A', 'bee', 1), ('B', 'geek', 2), ('C', 'python', 3)]
# (('A', 'bee', 1), ('B', 'geek', 2), ('C', 'python', 3))

# тест 2
sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(len(sequencezip))
print(sequencezip[1])
print(sequencezip[2])

# ответ
# 3
# ('B', 'geek', 2)
# ('C', 'python', 3)

# тест 3
print(len(SequenceZip([1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 4], 'data')))

# ответ
# 4
# 4
# 3

# тест 4
x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])

# ответ
# (3, 6, 9)
# (3, 6, 9)

# тест 5
many_large_sequences = [range(100000) for _ in range(100)]
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])

# ответ
# (99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999)

# тест 6
sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))

# ответ
# 0
# []

# тест 7
data = {'bee': 'bee', 'geek': 'geek'}

sequencezip = SequenceZip(data)
data['python'] = 'python'
print(data)
print(len(sequencezip))
print(list(sequencezip))

# ответ
# {'bee': 'bee', 'geek': 'geek', 'python': 'python'}
# 2
# [('bee',), ('geek',)]

# тест 8
data = {'bee': 'bee', 'geek': 'geek'}
sequencezip = SequenceZip(data)
print(sequencezip[0])
print(list(sequencezip))

# ответ
# ('bee',)
# [('bee',), ('geek',)]