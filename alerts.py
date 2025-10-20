from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1=browser.find_element(By.CSS_SELECTOR,"[type='submit']")
    button1.click()
    confirm=browser.switch_to.alert
    confirm.accept()
    x_value=browser.find_element(By.ID,"input_value").text
    print(x_value)
    x=math.log(abs(12*math.sin(int(x_value))))
    input1=browser.find_element(By.TAG_NAME,"input")
    input1.send_keys(x)
    submit1=browser.find_element(By.CSS_SELECTOR,"[type='submit']")
    submit1.click()
    alert=browser.switch_to.alert
    text=alert.text.split(" ")
    alert.accept()
    print(text[-1])
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # закрываем браузер после всех манипуляций
    browser.quit()