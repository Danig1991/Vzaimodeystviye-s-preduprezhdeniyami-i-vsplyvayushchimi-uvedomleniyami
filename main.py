import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# пауза
time.sleep(2)

# нажать JS Alert/перейти на уведомление/нажать ОК
driver_chrome.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
time.sleep(2)
driver_chrome.switch_to.alert.accept()
print("JS Alert отработано")

# пауза
time.sleep(2)

# нажать JS Confirm/перейти на уведомление/нажать отмена
driver_chrome.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
time.sleep(2)
driver_chrome.switch_to.alert.dismiss()
print("JS Confirm отработано")

# пауза
time.sleep(2)

# нажать JS Prompt/перейти на уведомление/ввести текст/нажать ОК
driver_chrome.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(2)
driver_chrome.switch_to.alert.send_keys("Test text!")
time.sleep(2)
driver_chrome.switch_to.alert.accept()
print("JS Prompt отработано")

# пауза
time.sleep(2)

# закрытие браузера
driver_chrome.quit()
print("Браузер закрыт.")
