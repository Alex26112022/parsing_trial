from config import path_logger
from src.parser import Parser
from src.write_csv import write_csv
from loguru import logger

rotation = '1 MB'  # максимальный размер лог-файла.
retention = '365 days'  # максимальное время хранения лог-файла.

logger.add(path_logger, format='{time} {level} {message}', level='DEBUG',
           rotation=rotation, retention=retention, compression='zip')


@logger.catch
def main():
    URL = 'https://kraevoi--krd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&H_date='  # noqa
    search_text = 'Иски о взыскании сумм по договору займа, кредитному договору'  # Ключевые слова поиска # noqa
    user_input = input('Введите дату поиска в формате: ДД.ММ.ГГГГ\n')
    new_parser = Parser(URL, user_input, search_text)
    print('Ждите! Идет загрузка данных...')
    new_parser.load_info()
    trials_list = new_parser.get_trial_list()
    print(f'Найдено {len(trials_list)} протоколов.')

    for trial in trials_list:
        write_csv(trial.num_trial, trial.date_trial, trial.referee,
                  trial.complainant, trial.respondent, trial.resolution)

    print('Данные успешно добавлены в CSV-файл.')


if __name__ == '__main__':
    main()
