class Elevator:
    def __init__(self, amount_flor=5, current_flor=3):
        self.amount_flor = amount_flor
        self.current_flor = current_flor

    def up(self):
        if self.current_flor < self.amount_flor:
            print(f'')
