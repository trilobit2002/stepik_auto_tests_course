from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC # модуль позволяет реализовывать различные ожидания
from selenium.webdriver.support.ui import WebDriverWait
import time # для использования задержки
import math
import os #для загрузки файла по кнопке

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:

    from selenium import webdriver
    from selenium.webdriver.common.by import By

    browser = webdriver.Chrome()
    #ждем когда цена снизится до 100 долларов
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    Price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    #нажимаем на кнопку  book
    button = browser.find_element(By.ID, "book")
    button.click()

    #считываем х и считаем формулу
    xz = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    xz = int(xz)
    fxz = calc(xz)
    # Ввести ответ в текстовое поле, прокрутив страницу
    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='text']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(fxz)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()
    #получаем текст алерта с ответом
    #print(browser.switch_to.alert.text)

    #python c:\Users\Office\selenium_course\2_4_8.py
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

    