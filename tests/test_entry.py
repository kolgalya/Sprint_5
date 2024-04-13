from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

class TestStellarBurgersEntry:
    def test_log_in_log_in_to_your_account(self, driver, user):
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.login).send_keys(user.get('mail'))
        driver.find_element(*Locators.password).send_keys(user.get('password'))
        driver.find_element(*Locators. button_entry).click()
        WDW(driver, 3).until(EC.element_to_be_clickable((Locators.burgers)))
        button_order = driver.find_element(*Locators.button_order)
        assert button_order.text == 'Оформить заказ'

    def test_log_in_log_in_to_your_personal_account(self, driver, user):
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.login).send_keys(user.get('mail'))
        driver.find_element(*Locators.password).send_keys(user.get('password'))
        driver.find_element(*Locators.button_entry).click()
        WDW(driver, 3).until(EC.element_to_be_clickable((Locators.burgers)))
        button_order = driver.find_element(*Locators.button_order)
        assert button_order.text == 'Оформить заказ'

    def test_login_registration_form(self, driver, user):
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.register).click()
        driver.find_element(*Locators.link_entry).click()
        driver.find_element(*Locators.login).send_keys(user.get('mail'))
        driver.find_element(*Locators.password).send_keys(user.get('password'))
        driver.find_element(*Locators.button_entry).click()
        WDW(driver, 3).until(EC.element_to_be_clickable((Locators.burgers)))
        assert driver.find_element(*Locators.button_order).text == 'Оформить заказ'

    def test_login_password_recovery_form(self, driver, user):
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.recover_password).click()
        driver.find_element(*Locators.entry_recover_password).click()
        driver.find_element(*Locators.login).send_keys(user.get('mail'))
        driver.find_element(*Locators.password).send_keys(user.get('password'))
        driver.find_element(*Locators.button_entry).click()
        WDW(driver, 3).until(EC.element_to_be_clickable((Locators.burgers)))
        assert driver.find_element(*Locators.button_order).text == 'Оформить заказ'



