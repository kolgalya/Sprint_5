"# Sprint_5" 

Тестирование сервиса Stellar Burgers по адресу https://stellarburgers.nomoreparties.site/.
Проект содержит папку tests с файлами тестов (13 тестов), файл с локаторами locators.py, файл фикстур, файл settings.py с URL.
Для запуска тестов - pytest -v. 

Описание тестов:
Регистрация: test_registration_in_personal_account.py 
    test_successful_registration - успешная регистрация
    test_invalid_password - регистрация с некорректным паролем

Вход: test_entry.py
    test_log_in_log_in_to_your_account - вход по кнопке «Войти в аккаунт» на главной
    test_log_in_log_in_to_your_personal_account - вход через кнопку «Личный кабинет»
    test_login_registration_form - вход через кнопку в форме регистрации
    test_login_password_recovery_form - вход через кнопку в форме восстановления пароля
    
Переход в личный кабинет: test_entry_in_personal_account.py
    test_in_to_your_personal_account - авторизация и вход в личный кабинет
    
Переход из личного кабинета в конструктор: test_switching_from_personal_account_to_constructor.py
    test_switching_in_constructor - переход по клику на «Конструктор» 
    test_switching_on_logo - переход по клику на логотип Stellar Burgers

Выход из аккаунта: test_exit_from_personal_account.py
    test_exit - успешный выход из аккаунта
    
Переход по разделам «Конструктор»: test_transition_to_ingredients.py
    test_transition_to_buns - переход к разделу «Булки»
    test_transition_to_sauce - переход к разделу «Соусы»
    test_transition_to_fillings - переход к разделу «Начинки»