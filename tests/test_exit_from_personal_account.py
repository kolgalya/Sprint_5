from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import settings
from locators import Locators


class TestStellarBurgersExit:
    def test_exit(self, driver, user):
        driver.find_element(*Locators.personal_account).click()
        driver.find_element(*Locators.login).send_keys(user.get('mail'))
        driver.find_element(*Locators.password).send_keys(user.get('password'))
        driver.find_element(*Locators.button_entry).click()
        driver.find_element(*Locators.personal_account).click()
        WDW(driver, 3).until(EC.visibility_of_element_located((Locators.profile)))
        driver.find_element(*Locators.button_exit).click()
        WDW(driver, 3).until(EC.element_to_be_clickable((Locators.button_entry)))
        assert driver.current_url == (settings.url + 'login')



