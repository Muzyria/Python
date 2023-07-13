class Selfie:
    def __init__(self):
        self.states = []
        self.current_state = {}

    def save_state(self):
        self.states.append(self.current_state.copy())

    def recover_state(self, index):
        if 0 <= index < len(self.states):
            new_selfie = Selfie()
            new_selfie.states = self.states[:index + 1]
            new_selfie.current_state = self.states[index].copy()
            return new_selfie
        else:
            return self

    def n_states(self):
        return len(self.states)

    def __setattr__(self, name, value):
        self.current_state[name] = value
        super().__setattr__(name, value)

    def __getattr__(self, name):
        return self.current_state.get(name, None)






obj = Selfie()

obj.x = 1
obj.y = 2

print(obj.x)
print(obj.y)

obj.save_state()
obj.x = 0
obj.y = 0

print(obj.x)
print(obj.y)
obj = obj.recover_state(0)
print(obj.x)
print(obj.y)


from string import ascii_lowercase

obj = Selfie()
for char in ascii_lowercase:
    obj.__dict__[char] = ord(char)

print(*(obj.__dict__[char] for char in ascii_lowercase))
obj.save_state()

for char in ascii_lowercase:
    obj.__dict__[char] = ord(char) + 100

print(*(obj.__dict__[char] for char in ascii_lowercase))
obj = obj.recover_state(0)

print(*(obj.__dict__[char] for char in ascii_lowercase))