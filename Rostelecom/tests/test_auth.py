import time
from time import sleep

from pages.auth_page import *

#RS-001 Проверка загрузки страницы
def test_main(driver):
    auth_page = AuthPage(driver)
    auth_page.load()
    assert auth_page.is_loaded()

#RS-002 Проверка расположения блоков на странице Авторизации (сохранить скриншот)
def test_vision(driver):
    auth_page = AuthPage(driver)
    auth_page.load()
    auth_page.is_loaded()
    auth_page.driver.save_screenshot('form.png')

#RS-003 Успешная проверка смены "плесхолдера" при переключении таба "Телефон", "Почта", "Логин", "Лицевой счет"
def test_tab_and_placeholder(driver):
    AuthForm(driver).tab_and_placeholder()

#RS-004 Успешная авторизация c корректным номером Телефона и Паролем
def test_auth(driver):
    AuthForm(driver).authorization_by_phone()

#RS-005 Не успешная авторизация по номеру Телефона с неверными данными
def test_auth_failed(driver):
    AuthForm(driver).failed_authorization_by_phone()

#RS-006 Успешная авторизация c корректной Почтой и Паролем
def test_auth_email(driver):
    AuthForm(driver).authorization_by_email()

#RS-007 Не успешная авторизация с не корректной Почтой и Паролем
def test_auth_failed_email(driver):
    AuthForm(driver).failed_authorization_by_email()

#RS-008 Успешная авторизация по Логину
def test_auth_login(driver):
    AuthForm(driver).authorization_by_login()

#RS-009 Не успешная авторизация с помощью неверного Логина и Пароля
def test_auth_failed_login(driver):
    AuthForm(driver).failed_authorization_by_login()

#RS-011 Не успешная авторизация с некорректным номером Лицевого счёта и Паролем
def test_auth_failed_personal_account(driver):
    AuthForm(driver).failed_authorization_by_personal_account()

#RS-019 Проверить основные элементы на странице Восстановление пароля
def test_vision_form_password_recovery(driver):
    AuthForm(driver).form_password_recovery()

#RS-022 Проверка основных элементов на странице форма регистрации
def test_vision_form_registration(driver):
    AuthForm(driver).form_registration()

#RS-023 Авторизация через соцсеть Вконтакте
def test_auth_by_vk(driver):
    AuthForm(driver).auth_by_vk()
    assert driver.current_url.startswith('https://id.vk.com/')

#RS-024 Авторизация через соцсеть Одноклассники
def test_auth_by_ok(driver):
    AuthForm(driver).auth_by_ok()
    assert driver.current_url.startswith('https://connect.ok.ru/')

#RS-025 Авторизация через соцсеть Мой мир
def test_auth_by_my_mail(driver):
    AuthForm(driver).auth_by_my_mail()
    assert driver.current_url.startswith('https://connect.mail.ru/')

#RS-026 Авторизация через Паспорт Яндекс !!!
def test_auth_by_ya(driver):
    AuthForm(driver).auth_by_ya()
    time.sleep(10)
    assert driver.current_url.startswith('https://passport.yandex.ru/')

#RS-027 Корректная работа ссылки с Политикой конфиденциальности !!!
def test_privacy_policy(driver):
    AuthForm(driver).privacy_policy()
    assert driver.current_url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

#RS-028 Корректная работа ссылки с Пользовательского соглашения !!!
def test_user_agreement(driver):
    AuthForm(driver).user_agreement()
    assert driver.current_url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

#RS-029 Авторизация с пустым полем Телефон
def test_authorization_with_empty_phone(driver):
    AuthForm(driver).failed_authorization_with_empty_phone()

#RS-030 Авторизация с пустым полем Почта
def test_authorization_with_empty(driver):
    AuthForm(driver).failed_authorization_with_empty()

#RS-031 Авторизация с пустым полем Логин
def test_authorization_with_empty_login(driver):
    AuthForm(driver).failed_authorization_with_empty_login()

#RS-032 Авторизация с пустым полем Лицевой счёт
def test_authorization_with_empty_personal_account(driver):
    AuthForm(driver).failed_authorization_with_empty_personal_account()