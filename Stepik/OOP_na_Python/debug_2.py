
def get_info_marks(students: list[str], *marks: list) -> dict[str, dict[str, int]]:
    return dict(zip(students, [{'best': max(m), 'worst': min(m)} for m in zip(*marks)]))



math = [90, 76, 94]
history = [78, 79, 90]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students, math, history))