from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import settings

class TestStellarBurgersRegistration:
    def test_successful_registration(self, driver, correct_email, correct_password):
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.register).click()
        driver.find_element(*Locators.name_register).send_keys("Galya")
        driver.find_element(*Locators.mail_register).send_keys(correct_email)
        driver.find_element(*Locators.password_register).send_keys(correct_password)
        driver.find_element(*Locators.button_register).click()
        WDW(driver, 3).until(EC.element_to_be_clickable((Locators.button_entry)))
        assert driver.current_url == (settings.url + 'login')


    def test_invalid_password(self, driver, correct_email, invalid_password):
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.register).click()
        driver.find_element(*Locators.name_register).send_keys("Galya")
        driver.find_element(*Locators.mail_register).send_keys(correct_email)
        driver.find_element(*Locators.password_register).send_keys(invalid_password)
        driver.find_element(*Locators.button_register).click()
        error = driver.find_element(*Locators.error)
        assert error.get_attribute('class') == 'input__error text_type_main-default'





