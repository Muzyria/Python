from dataclasses import dataclass, field

@dataclass
class Person:
    first_name: str
    last_name: str
    hobbies: set = field(default_factory=set)


hobbies = ["спорт", "чтение", "йога", "спорт", "музыка", "танцы", "путешествия", "кино",
           "фотография", "музыка", "танцы", "йога", "рисование", "кулинария", "танцы",
           "садоводство", "йога", "спорт", "велоспорт", "шахматы", "йога",
           "танцы", "путешествия", "рыбалка", "походы", "спорт",
           "кулинария", "плавание", "танцы", "музыка",
           "спорт", "йога"]

ivan = Person("Иван", "Иванов")
anna = Person("Анна", "Смирнова")
petr = Person("Петр", "Петров", {"спорт", "скандинавская ходьба"})

for i, hobby in enumerate(hobbies):
    if i % 3 == 0:
        ivan.hobbies.add(hobby)
    elif i % 3 == 1:
        anna.hobbies.add(hobby)
    else:
        petr.hobbies.add(hobby)

print(sorted(ivan.hobbies))
print(sorted(anna.hobbies))
print(sorted(petr.hobbies))
