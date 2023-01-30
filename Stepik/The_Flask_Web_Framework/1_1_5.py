class Elevator:
    def __init__(self, amount_flor=5, current_flor=3):
        self.amount_flor = amount_flor
        self.current_flor = current_flor

    def up(self):
        if self.current_flor < self.amount_flor:
            self.current_flor += 1
            print(f'Лифт поднимается на {self.current_flor} этаж')
        else:
            print('Лифт не может подняться выше')

    def down(self):
        if self.current_flor > 1:
            self.current_flor -= 1
            print(f'Лифт опускается на {self.current_flor} этаж')
        else:
            print('Лифт не может опуститься ниже')