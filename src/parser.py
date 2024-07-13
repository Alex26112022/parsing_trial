from datetime import datetime
from time import sleep

from fake_headers import Headers
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm

from config import path_logger
from src.trial_object import Trial


class Parser:
    """ Класс-парсер сайта. """

    def __init__(self, url: str, date_trial: str, search_text: str):
        self.__URL = url
        self.date_trial = date_trial
        self.trial_list = []
        self.search_text = search_text

        headers = Headers(os="win", headers=True).generate()['User-Agent']
        options = webdriver.ChromeOptions()

        options.add_argument(f'user-agent={headers}')
        # Отключение режима драйвера.
        options.add_argument('--disable-blink-features=AutomationControlled')
        # Работа в фоновом режиме.
        options.add_argument('headless')

        # Инициализация драйвера Chrome.
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)

        self.search_text = 'Иски о взыскании сумм по договору займа, кредитному договору'  # noqa

    def load_info(self):
        """ Загружает информацию. """
        try:
            self.driver.get(url=self.__URL + self.date_trial)
            sleep(10)
            trials = self.driver.find_elements(By.XPATH, '//tr[@valign="top"]')
            for trial in tqdm(trials):

                full_info = trial.find_elements(By.TAG_NAME, 'td')

                if self.search_text not in full_info[5].text:
                    continue

                number_trial = full_info[1].text
                referee = full_info[6].text
                complainant_respondent = full_info[5].text.split(':')
                complainant = ' '.join(complainant_respondent[2].split()[:-1])
                respondent = ' '.join(complainant_respondent[3].split()[:-3])
                resolution = full_info[7].text

                self.trial_list.append(
                    Trial(number_trial, self.date_trial, referee, complainant,
                          respondent, resolution))

        except Exception as e:
            with open(path_logger, 'a', encoding='utf-8') as file_log:
                file_log.write(f'{datetime.now()}\nError: {e}')
            print(e)
        finally:
            self.driver.close()
            self.driver.quit()

    def get_trial_list(self) -> list[Trial]:
        """ Возвращает список экземпляров класса Trial. """
        return self.trial_list
