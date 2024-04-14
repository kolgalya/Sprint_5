import pytest
import settings
import random
import string
from selenium import webdriver

@pytest.fixture()
def driver():
    chrom_driver = webdriver.Chrome()
    chrom_driver.maximize_window()
    chrom_driver.get(settings.url)
    yield chrom_driver
    chrom_driver.quit()

@pytest.fixture()
def correct_email():
    correct_email = str(random.choice(string.ascii_letters))*3 + str(random.randint(100,999)) + '@mail.ru'
    return correct_email

@pytest.fixture()
def correct_password():
    correct_password = random.randint(100000,999999)
    return correct_password

@pytest.fixture()
def invalid_password():
    invalid_password = random.randint(100,999)
    return invalid_password

@pytest.fixture()
def user():
    user = {'mail' : 'kolgalya@ya.ru', 'password' : '123456'}
    return user


