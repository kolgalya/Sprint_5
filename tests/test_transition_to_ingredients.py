from locators import Locators

class TestStellarBurgersIngredient:
    def test_transition_to_buns(self, driver):
        ingredient = driver.find_element(*Locators.last_ingredient)
        driver.execute_script("arguments[0].scrollIntoView();",ingredient)
        driver.find_element(*Locators.link_buns).click()
        buns = driver.find_element(*Locators.buns)
        assert 'tab_tab_type_current' in buns.get_attribute('class')

    def test_transition_to_sauce(self, driver):
        driver.find_element(*Locators.link_sauce).click()
        sauce = driver.find_element(*Locators.sauce)
        assert 'tab_tab_type_current' in sauce.get_attribute('class')

    def test_transition_to_fillings(self, driver):
        driver.find_element(*Locators.link_fillings).click()
        fillings = driver.find_element(*Locators.fillings)
        assert 'tab_tab_type_current' in fillings.get_attribute('class')

