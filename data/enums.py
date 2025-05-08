from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Subject(Enum):
    COMPUTER_SCIENCE = "Computer Science"
    PHYSICS = "Physics"


class Hobby(Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"
