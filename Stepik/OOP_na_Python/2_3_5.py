
class CustomLabel:
    def __init__(self, text, **kwargs):
        self.text = text
        self.config(**kwargs) # Обращение к методу config класса CustomLabel.

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        


label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')

print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}

label.config(color='red', bd=100)

print(label.__dict__) # {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}