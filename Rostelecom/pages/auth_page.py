import time
from pages.settings import *
from .locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class AuthPage:

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get('https://b2c.passport.rt.ru/')

    def is_loaded(self) -> bool:
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(Locators.username_locator))
            return True
        except:
            return False

class AuthForm(AuthPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.load()
        self.is_loaded()
        self.wait = WebDriverWait(self.driver, timeout=10)

    #RS-003 Успешная проверка автосмены "плесхолдера" при переключении таба "Телефон", "Почта", "Логин", "Лицевой счет"
    def tab_and_placeholder(self):
        self.driver.find_element(*Locators.username_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.placeholder, text_="Мобильный телефон"))
        self.driver.find_element(*Locators.email_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.placeholder, text_="Электронная почта"))
        self.driver.find_element(*Locators.login_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.placeholder, text_="Логин"))
        self.driver.find_element(*Locators.personal_account).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.placeholder, text_="Лицевой счёт"))

    #RS-004 Успешная авторизация c корректным номером Телефона и Паролем
    def authorization_by_phone(self):
        self.driver.find_element(*Locators.username_locator).send_keys(valid_phone)
        time.sleep(20)  # Тест может потребовать ввести капчу. В таком случае нужно ввести вручную
        self.driver.find_element(*Locators.password_locator).send_keys(valid_pass)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.user_name, text_="Фёдоров"), message='login failed')
        print("login success")

    #RS-005 Не успешная авторизация по номеру Телефона с неверными данными
    def failed_authorization_by_phone(self):
        self.driver.find_element(*Locators.username_locator).send_keys(invalid_phone)
        time.sleep(20)  # Тест может потребовать ввести капчу. В таком случае нужно ввести вручную
        self.driver.find_element(*Locators.password_locator).send_keys(invalid_pass)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message, text_="Неверный логин или пароль"))
        print("login failed")

    #RS-006 Успешная авторизация c корректной Почтой и Паролем
    def authorization_by_email(self):
        self.driver.find_element(*Locators.email_locator).click()
        time.sleep(20)  # Тест может потребовать ввести капчу. В таком случае нужно ввести вручную
        self.driver.find_element(*Locators.username_locator).send_keys(valid_email)
        self.driver.find_element(*Locators.password_locator).send_keys(valid_pass_email)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.user_name, text_="Фёдоров"), message='login failed')
        print("login success")

    #RS-007 Не успешная авторизация с помощью не корректной Почты и Пароля
    def failed_authorization_by_email(self):
        self.driver.find_element(*Locators.email_locator).click()
        time.sleep(20)  # Тест может потребовать ввести капчу. В таком случае нужно ввести вручную
        self.driver.find_element(*Locators.username_locator).send_keys(invalid_email)
        self.driver.find_element(*Locators.password_locator).send_keys(invalid_pass_email)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message, text_="Неверный логин или пароль"))
        print("login failed")

    #RS-008 Успешная авторизация клиента по Логину
    def authorization_by_login(self):
        self.driver.find_element(*Locators.login_locator).click()
        time.sleep(20)  # Тест может потребовать ввести капчу. В таком случае нужно ввести вручную
        self.driver.find_element(*Locators.username_locator).send_keys(valid_login)
        self.driver.find_element(*Locators.password_locator).send_keys(valid_pass)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.user_name, text_="Фёдоров"), message='login failed')
        print("login success")

    #RS-009 Не успешная авторизация с помощью неверного Логина и Пароля
    def failed_authorization_by_login(self):
        self.driver.find_element(*Locators.login_locator).click()
        time.sleep(20)  # Тест может потребовать ввести капчу. В таком случае нужно ввести вручную
        self.driver.find_element(*Locators.username_locator).send_keys(invalid_login)
        self.driver.find_element(*Locators.password_locator).send_keys(invalid_pass)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message, text_="Неверный логин или пароль"))
        print("login failed")

    #RS-011 Не успешная авторизация с некорректными номером Лицевого счёта и Паролем.
    def failed_authorization_by_personal_account(self):
        self.driver.find_element(*Locators.personal_account).click()
        time.sleep(20) #Тест может потребовать ввести капчу. В таком случае нужно ввести вручную
        self.driver.find_element(*Locators.username_locator).send_keys(invalid_account)
        self.driver.find_element(*Locators.password_locator).send_keys(invalid_pass)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message, text_="Неверный логин или пароль"))
        print("login failed")

    #RS-019 Проверить основные элементы на странице Восстановление пароля
    def form_password_recovery(self):
        self.driver.find_element(*Locators.password_recovery).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.title, text_="Восстановление пароля"))
        self.driver.save_screenshot('form_password_recover.png')

    #RS-022 Проверка основных элементов на странице форма регистрации
    def form_registration(self):
        self.driver.find_element(*Locators.registration).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.title, text_="Регистрация"))
        self.driver.save_screenshot('form_registration.png')

    #RS-023 Авторизация через соцсеть Вконтакте
    def auth_by_vk(self):
        self.driver.find_element(*Locators.vk).click()

    #RS-024 Авторизация через соцсеть Одноклассники
    def auth_by_ok(self):
        self.driver.find_element(*Locators.ok).click()

    #RS-025 Авторизация через соцсеть Мой мир
    def auth_by_my_mail(self):
        self.driver.find_element(*Locators.my_mail).click()

    #RS-026 Авторизация через Паспорт Яндекс
    def auth_by_ya(self):
        self.driver.find_element(*Locators.ya).click()

    #RS-027 Корректная работа ссылки с Политикой конфиденциальности
    def privacy_policy(self):
        self.driver.find_element(*Locators.privacy_policy).click()

    #RS-028 Корректная работа ссылки с Пользовательского соглашения
    def user_agreement(self):
        self.driver.find_element(*Locators.user_agreement).click()

    #RS-029 Авторизация с пустым полем Телефон
    def failed_authorization_with_empty_phone(self):
        self.driver.find_element(*Locators.phone_locator).click()
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message_pole, text_="Введите номер телефона"))
        print("empty field")

    #RS-030 Авторизация с пустым полем Почта
    def failed_authorization_with_empty(self):
        self.driver.find_element(*Locators.email_locator).click()
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message_pole, text_="Введите адрес, указанный при регистрации"))
        print("empty field")

    #RS-031 Авторизация с пустым полем Логин
    def failed_authorization_with_empty_login(self):
        self.driver.find_element(*Locators.login_locator).click()
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message_pole, text_="Введите логин, указанный при регистрации"))
        print("empty field")

    #RS-032 Авторизация с пустым полем Лицевой счёт
    def failed_authorization_with_empty_personal_account(self):
        self.driver.find_element(*Locators.personal_account).click()
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message_pole, text_="Введите номер вашего лицевого счета"))
        print("empty field")