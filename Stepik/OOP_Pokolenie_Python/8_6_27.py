from dataclasses import dataclass, field

@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)

@dataclass
class FootballTeam:
    name: str
    players: list = field(default_factory=list, repr=False)

    def __post_init__(self):
        if self.players is None:
            self.players = []

    def add_players(self, *args):
        self.players.extend(args)


team = FootballTeam('PSG')

print(team)
print(team.name)
print(team.players)

team.add_players(FootballPlayer('Kylian', 'Mbappe', 180000000))
print(team.players)