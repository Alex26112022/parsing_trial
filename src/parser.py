from time import sleep

from fake_headers import Headers
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://kraevoi--krd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&H_date='
date_trial = '11.07.2024'

headers = Headers(os="win", headers=True).generate()['User-Agent']
options = webdriver.ChromeOptions()

options.add_argument(f'user-agent={headers}')
# Отключение режима драйвера.
options.add_argument('--disable-blink-features=AutomationControlled')

# Инициализация драйвера Chrome.
driver = webdriver.Chrome(options=options)

number_trial_list = []  # Список номеров дел.
referees_list = []  # Список судей.
complainants_list = []  # Список истцов.
respondent_list = []  # Список ответчиков.
resolution_list = []  # Список решений.
search_text = 'Иски о взыскании сумм по договору займа, кредитному договору'

try:
    driver.get(url=URL + date_trial)
    sleep(10)
    trials = driver.find_elements(By.XPATH, '//tr[@valign="top"]')
    for trial in trials:

        full_info = trial.find_elements(By.TAG_NAME, 'td')

        if search_text not in full_info[5].text:
            continue

        number_trial = full_info[1]
        number_trial_list.append(number_trial.text)

        referee = full_info[6]
        referees_list.append(referee.text)

        complainant_respondent = full_info[5].text.split(':')

        complainant = complainant_respondent[2].split()[:-1]
        complainants_list.append(' '.join(complainant))

        respondent = complainant_respondent[3].split()[:-3]
        respondent_list.append(' '.join(respondent))

        resolution = full_info[7]
        resolution_list.append(resolution.text)


except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
