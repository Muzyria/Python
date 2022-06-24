class CustomLabel:
    def __init__(self, text, **kwargs):
        self.text = text
        print(kwargs)
        #for key, value in kwargs.items():
            #self.__dict__[key] = value

    def config(self, **kwargs):
        print(kwargs)
        #self.__dict__.update(kwargs)


label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')

#print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}

#label.config(color='red', bd=100)

#print(label.__dict__) # {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}