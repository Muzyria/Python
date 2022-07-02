class CustomButton:
    def __init__(self, text, **kwargs):
        self.text = text
        self.config(**kwargs) # Обращение к методу config класса CustomButton.

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)  

    def click(self):
        try:
            self.command()   
        except AttributeError:
            print("Кнопка не настроена")
        except TypeError:
            print("Кнопка сломалась")    



def func():
    print('Оно живое')


btn = CustomButton(text="Hello", bd=20, bg='#ffaaaa')
btn.click()  # Кнопка не настроена
btn.config(command=func)
btn.click()  # Оно живое
print(btn.__dict__)
