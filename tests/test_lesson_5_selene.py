'''
https://github.com/chaenkova/selene_hw/blob/master/tests/selene_hw_test.py
https://github.com/almatyAlma/selen-in-action-py13-5/blob/master/tests/test_todo_operations.py
https://github.com/ilichev-art/demoqa-test/blob/main/tests/test_demoqa.py
'''
import os
from os.path import dirname, abspath
from selene import browser, have


def test_fill_registration_form_and_submit():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').should(have.attribute('placeholder').value('First Name')).type('Ivan')
    browser.element('#lastName').should(have.attribute('placeholder').value('Last Name')).type('Ivanov')
    browser.element('#userEmail').should(have.attribute('placeholder').value('name@example.com')).type('ivanov@gmail.com')

    browser.all('#genterWrapper label').should(have.exact_texts('Male', 'Female', 'Other')).element_by(
        have.exact_text('Male')).click()

    browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number')).type('9999999999')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select>option').element_by(have.exact_text('January')).click()

    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select>option').element_by(have.exact_text('2000')).click()
    browser.all('.react-datepicker__month .react-datepicker__day').element_by(have.exact_text('1')).click()

    browser.element('#subjectsInput').type("p").press_tab()

    browser.all('#hobbiesWrapper label[title]').should(have.exact_texts('Sports', 'Reading', 'Music')).element_by(
        have.exact_text('Sports')).click()

    browser.element('#uploadPicture').send_keys(os.path.join(os.path.join(dirname(dirname(abspath(__file__))), "resources", 'foto.jpg')))

    browser.element('#currentAddress').should(have.attribute('placeholder').value('Current Address')).type('Moscow, Kremlin')

    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()

    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').click()

    browser.element('.modal-content').element('table').all('tr').all('td').even.should(
        have.exact_texts(
            'Ivan Ivanov',
            'ivanov@gmail.com',
            'Male',
            '9999999999',
            '01 January,2000',
            'Physics',
            'Sports',
            'foto.jpg',
            'Moscow, Kremlin',
            'NCR Delhi',
        )
    )
