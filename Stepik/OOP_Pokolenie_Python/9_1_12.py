import copy

class Selfie:
    def __init__(self):
        self.states = []
        self.current_state = None

    def save_state(self):
        state = {}
        for attr, value in self.__dict__.items():
            if attr != 'states' and attr != 'current_state':
                state[attr] = value
        self.states.append(state)
        self.current_state = state

    def recover_state(self, index):
        if index < len(self.states):
            state = copy.deepcopy(self.states[index])
            obj = Selfie()
            for attr, value in state.items():
                setattr(obj, attr, value)
            obj.states = self.states
            obj.current_state = state
            return obj
        else:
            return self

    def n_states(self):
        return len(self.states)




def sum_a_b(a, b):
    return a + b


def sub_a_b(a, b):
    return a - b


def mul_a_d(a, b):
    return a * b


def truediv_a_b(a, b):
    return a / b


obj = Selfie()
obj.sum_a_b = sum_a_b
print(obj.sum_a_b(1, 2))
obj.save_state()

obj.sub_a_b = sub_a_b
print(obj.sub_a_b(1, 2))
obj.save_state()

obj.mul_a_d = mul_a_d
print(obj.mul_a_d(1, 2))
obj.save_state()

obj.truediv_a_b = truediv_a_b
print(obj.truediv_a_b(1, 2))
obj.save_state()

print(obj.n_states())
obj = obj.recover_state(1)

print(obj.n_states())
