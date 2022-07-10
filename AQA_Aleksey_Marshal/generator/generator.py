import random

from data.data import Person
from faker import Faker

faker_en = Faker("En")


def generated_person():
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        mobile=faker_en.msisdn(),
        subject="English"
    )


def generated_file():
    path = rf"C:\Git_Muzyria\Python\AQA_Aleksey_Marshal\test{random.randint(10, 100)}.txt"
    with open(path, "w") as file:
        file.write(f"Helloworld {random.randint(10, 100)}")
    return path

