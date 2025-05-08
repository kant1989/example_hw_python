from data import users
from pages.application import app


def test_student_registration_form():
    app.registration_page.open()

    # WHEN
    app.registration_page.register(users.student)

    # THEN
    app.registration_page.should_have_registered(users.student)
