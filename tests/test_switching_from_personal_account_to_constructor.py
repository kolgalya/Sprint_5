from locators import Locators
import settings

class TestStellarBurgersConstructor:
    def test_switching_in_constructor(self, driver, user):
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.login).send_keys(user.get('mail'))
        driver.find_element(*Locators.password).send_keys(user.get('password'))
        driver.find_element(*Locators.button_entry).click()
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.link_constructor).click()
        assert driver.current_url == settings.url



    def test_switching_on_logo(self, driver, user):
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.login).send_keys(user.get('mail'))
        driver.find_element(*Locators.password).send_keys(user.get('password'))
        driver.find_element(*Locators.button_entry).click()
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.link_logo).click()
        assert driver.current_url == settings.url

