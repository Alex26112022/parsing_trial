import csv
import os

from config import path_trial


def write_csv(num_trial, date_trial, referee, complainant, respondent,
              resolution):
    """ Записывает данные в csv-файл. """
    csv_file_exists = os.path.isfile(path_trial)
    with (open(path_trial, 'a', encoding='utf-8', newline='') as
          csvfile):
        fieldnames = ['Номер дела', 'Дата заседания', 'Судья', 'Истец',
                      'Ответчик', 'Статус дела']
        if not csv_file_exists:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    with open(path_trial, 'a', encoding='utf-8', newline='') as file:
        field = ['Номер дела', 'Дата заседания', 'Судья', 'Истец',
                 'Ответчик', 'Статус дела']
        wr = csv.DictWriter(file, fieldnames=field)
        wr.writerow({'Номер дела': num_trial, 'Дата заседания': date_trial,
                     'Судья': referee, 'Истец': complainant,
                     'Ответчик': respondent, 'Статус дела': resolution})


if __name__ == '__main__':
    pass
