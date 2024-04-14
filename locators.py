from typing import Tuple

from selenium.webdriver.common.by import By

class Locators:
    personal_account = (By.LINK_TEXT, "Личный Кабинет") # Личный кабинет
    register = (By.LINK_TEXT, "Зарегистрироваться") # кнопка Зарегистрироваться из личного кабинета
    name_register = (By.XPATH, ".//label[text()='Имя']/following-sibling::input") # поле Имя при регистриации
    mail_register = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # поле Email при регистриации
    password_register = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") # поле Пароль при регистриации
    button_register = (By.XPATH, ".//button[contains(@class,'button_button__')]") # кнопка Зарегистрироваться в форме регистрации
    error = (By.XPATH, ".//p[text()='Некорректный пароль']") #Ошибка - некорректный пароль
    button_entry = (By.XPATH, ".//button[text() = 'Войти']")  # кнопка Войти в окне входа
    button_personal_account = (By.XPATH, ".//button[contains(@class,'button_button__')]")  # кнопка Войти в аккаунт на главной странице
    login = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # поле Email при входе
    password = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # поле Пароль при входе
    button_order = (By.XPATH, ".//button[contains(@class,'button_button__')]")  # кнопка Оформить заказ на главной странице
    burgers = (By.XPATH, ".//h1[contains(text(),'бургер')]") # кнопка Оформить заказ на главной странице
    link_entry = (By.XPATH, ".//p/a[contains(@class, 'Auth_link')]") # кнопка Войти на странице регистрации
    recover_password = (By.XPATH, ".//a[contains(@class, 'Auth_link')]") # кнопка Восстановить пароль на странице регистрации
    entry_recover_password = (By.XPATH, ".//a[contains(@class, 'Auth_link')]") # кнопка Войти на странице Восстановить пароль
    button_save = (By.XPATH, ".//button[text() = 'Сохранить']") #кнопка Сохранить в личном кабинете
    input_login = (By.XPATH, ".//input[@type='text' and @name='name']")  # поле Email в личном кабинете
    link_constructor = (By.XPATH, ".//li/a[@href='/']/p")  # ссылка Конструктор в личном кабинете
    link_logo = (By.XPATH, ".//div[contains(@class,'logo')]")  # ссылка Логотип в личном кабинете
    button_exit = (By.XPATH, ".//button[text() = 'Выход']")  # кнопка Выход в личном кабинете
    profile = (By.XPATH, ".//a[@href = '/account/profile']") # кнопка Профиль в личном кабинете
    last_ingredient = (By.XPATH, ".//div[contains(@class,'menuContainer')]/ul[3]/a[last()]")  # последний ингредиент на главной странице
    link_buns = (By.XPATH, ".//div[contains(@class, 'tab_tab')]/span[text() = 'Булки']")  # не активированная ссылка на Булки
    buns = (By.XPATH, ".//span[text() = 'Булки']/parent::div")  # активированная ссылка на Булки
    link_sauce = (By.XPATH, ".//div[contains(@class, 'tab_tab')]/span[text() = 'Соусы']")  # не активированная ссылка на Соусы
    sauce = (By.XPATH, ".//span[text() = 'Соусы']/parent::div")  # активированная ссылка на Соусы
    link_fillings = (By.XPATH, ".//div[contains(@class, 'tab_tab')]/span[text() = 'Начинки']")  # не активированная ссылка на Начинки
    fillings = (By.XPATH, ".//span[text() = 'Начинки']/parent::div")  # активированная ссылка на Начинки






