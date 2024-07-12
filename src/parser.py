from time import sleep

from fake_headers import Headers
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://kraevoi--krd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&H_date='
date_trial = '08.07.2024'

headers = Headers(os="win", headers=True).generate()['User-Agent']
options = webdriver.ChromeOptions()

options.add_argument(f'user-agent={headers}')
# Отключение режима драйвера.
options.add_argument('--disable-blink-features=AutomationControlled')

# Инициализация драйвера Chrome.
driver = webdriver.Chrome(options=options)

number_trial_list = []  # Список номеров дел.

try:
    driver.get(url=URL+date_trial)
    sleep(10)
    trials = driver.find_elements(By.XPATH, '//tr[@valign="top"]')
    for trial in trials:
        number_trial = trial.find_element(By.TAG_NAME, 'a')
        number_trial_list.append(number_trial.text)
    print(number_trial_list)

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
