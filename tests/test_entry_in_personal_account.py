from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestStellarBurgersPersonalAccount:
    def test_in_to_your_personal_account(self, driver, user):
        driver.find_element(*Locators.button_personal_account).click()
        driver.find_element(*Locators.login).send_keys(user.get('mail'))
        driver.find_element(*Locators.password).send_keys(user.get('password'))
        driver.find_element(*Locators.button_entry).click()
        driver.find_element(*Locators.personal_account).click()
        WDW(driver, 3).until(EC.element_to_be_clickable((Locators.button_save)))
        login = driver.find_element(*Locators.input_login)
        assert login.get_attribute('value') == user.get('mail')

