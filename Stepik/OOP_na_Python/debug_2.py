from dataclasses import dataclass, field

@dataclass(order=True)
class Athlet:
    sort_index: int = field(init=False, repr=False)
    name: str
    coefficient: float = field(repr=False)
    scores: list = field(default_factory=list, repr=False)

    def __post_init__(self):
        self.sort_index = sum(self.scores) / len(self.scores) * self.coefficient


sportsmans = [
    Athlet('Иван', 1.5, [9.0, 8.0, 7.0]),
    Athlet('Петр', 1.0, [10.0, 9.0, 8.0]),
    Athlet('Алексей', 1.2, [8.0, 7.0, 6.0])
]

print(f"Победитель соревнований: {max(sportsmans)}")