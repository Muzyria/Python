class Gun:
    def __init__(self) -> None:
        self._turn = False
        self.count_shoot = 0

    def shoot(self):
        print(('pif', 'paf')[self._turn])
        self._turn = not self._turn
        self.count_shoot += 1

    def shots_count(self):
        return self.count_shoot

    def shots_reset(self):
        self.count_shoot = 0
