class Pet:
    PETS = []

    def __init__(self, name):
        self.name = name
        Pet.PETS.append(self)

    @classmethod
    def first_pet(cls):
        if cls.PETS:
            return cls.PETS[0]
        return None

    @classmethod
    def last_pet(cls):
        if cls.PETS:
            return cls.PETS[-1]
        return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.PETS)


print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())

pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())

