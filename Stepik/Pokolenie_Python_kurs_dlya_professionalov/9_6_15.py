def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}


info = {'name': 'Timur', 'grades': [30, 57, 99]}
print(top_grade(info))
# {'name': 'Timur', 'top_grade': 99}

annotations = top_grade.__annotations__
print(annotations['grades'])
# dict[str, str | list[int]]

print(*top_grade.__annotations__.values())
# dict[str, str | list[int]] dict[str, str | int]
