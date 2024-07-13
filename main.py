from src.parser import Parser
from src.write_csv import write_csv


def main():
    URL = 'https://kraevoi--krd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&H_date='
    new_parser = Parser(URL, '11.07.2024')
    new_parser.load_info()
    trials_list = new_parser.get_trial_list()

    for trial in trials_list:
        write_csv(trial.num_trial, trial.date_trial, trial.referee,
                  trial.complainant, trial.respondent, trial.resolution)


if __name__ == '__main__':
    main()
