import allure

from data import users
from pages.application import app


@allure.label("owner", "Kantemir Koshiev")
@allure.feature("Регистрация")
@allure.story("Регистрация студента")
def test_student_registration_form():
    """
    Регистрация пользователя и проверка данных пользователя после регистрации
    """
    app.registration_page.open()

    # WHEN
    app.registration_page.register(users.student)

    # THEN
    app.registration_page.should_have_registered(users.student)
