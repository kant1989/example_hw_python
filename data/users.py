from datetime import date
from dataclasses import dataclass
from data.enums import Gender, Subject, Hobby


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    date_of_birth: date
    subjects: list[Subject]
    hobbies: list[Hobby]
    picture: str
    address: str
    state: str
    city: str


student = User(
    first_name="Olga",
    last_name="YA",
    email="name@example.com",
    gender=Gender.FEMALE.value,
    phone_number="1234567891",
    date_of_birth=date(1999, 5, 1),
    subjects=[Subject.COMPUTER_SCIENCE.value, Subject.PHYSICS.value],
    hobbies=[Hobby.SPORTS.value, Hobby.READING.value],
    picture="foto.jpg",
    address="Moscowskaya Street 18",
    state="NCR",
    city="Delhi",
)
