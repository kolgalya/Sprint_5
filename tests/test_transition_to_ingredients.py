from locators import Locators

class TestStellarBurgersIngredient:
    def test_transition_to_buns(self, driver):
        ingredient = driver.find_element(*Locators.last_ingredient)
        driver.execute_script("arguments[0].scrollIntoView();",ingredient)
        driver.find_element(*Locators.link_buns).click()
        buns = driver.find_element(*Locators.buns)
        assert 'tab_tab_type_current' in buns.get_attribute('class')


    def test_transition_to_sauce(self, driver):
        sauce_before = driver.find_element(*Locators.link_sauce)
        sauce_before.click()
        sauce_after = driver.find_element(*Locators.sauce)
        assert sauce_before.get_attribute('class') != sauce_after.get_attribute('class')


    def test_transition_to_fillings(self, driver):
        fillings_before = driver.find_element(*Locators.link_fillings)
        fillings_before.click()
        fillings_after = driver.find_element(*Locators.fillings)
        assert fillings_before.get_attribute('class') != fillings_after.get_attribute('class')

