import os

from selene import browser, have, command
import resources
from data.users import User


class RegistrationPage:

    def __init__(self):
        self.google_ads = "[id^=google_ads][id$=container__]"
        self.select_option = "[id^=react-select][id*=option]"

    def open(self):
        browser.open("/automation-practice-form")
        browser.all(self.google_ads).with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all(self.google_ads).perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def select_gender(self, value):
        browser.all("[name=gender]").element_by(have.value(value)).element("..").click()
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def fill_phone_number(self, value):
        browser.element("#userNumber").type(value)
        return self

    def select_hobbies(self, *args):
        for hobby in args:
            browser.all("label[for^=hobbies-checkbox]").element_by(
                have.exact_text(hobby)
            ).click()
        return self

    def fill_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def select_state(self, value):
        browser.element("#state").click()
        browser.all(self.select_option).element_by(have.exact_text(value)).click()
        return self

    def select_city(self, value):
        browser.element("#city").click()
        browser.all(self.select_option).element_by(have.exact_text(value)).click()
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

    def fill_subjects(self, *args):
        for subject in args:
            browser.element("#subjectsInput").type(subject).press_enter()
        return self

    def select_picture(self, filename):
        browser.element("#uploadPicture").set_value(
            os.path.abspath(os.path.join(os.path.dirname(resources.__file__), filename))
        )
        return self

    def submit(self):
        browser.element("#submit").press_enter()
        return self

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.fill_date_of_birth(
            user.date_of_birth.strftime("%Y"),
            user.date_of_birth.strftime("%B"),
            user.date_of_birth.strftime("%d"),
        )
        self.fill_subjects(*user.subjects)
        self.select_hobbies(*user.hobbies)
        self.select_picture(user.picture)
        self.fill_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)
        self.submit()
        return self

    def should_have_registered(self, user: User):
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                f"{user.first_name} {user.last_name}",
                user.email,
                user.gender,
                user.phone_number,
                f'{user.date_of_birth.strftime("%d")} {user.date_of_birth.strftime("%B")},{user.date_of_birth.strftime("%Y")}',
                ", ".join(user.subjects),
                ", ".join(user.hobbies),
                user.picture,
                user.address,
                f"{user.state} {user.city}",
            )
        )
