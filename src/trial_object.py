class Trial:
    """ Класс-объект судебного дела. """

    def __init__(self, num_trial, date_trial, referee, complainant, respondent,
                 resolution):
        self.num_trial = num_trial
        self.date_trial = date_trial
        self.referee = referee
        self.complainant = complainant
        self.respondent = respondent
        self.resolution = resolution

    def __str__(self):
        return (f'Номер дела: {self.num_trial}\nДата дела: {self.date_trial}\n'
                f'Судья: {self.referee}\nИстец: {self.complainant}\n'
                f'Ответчик: {self.respondent}\nРешение: {self.resolution}')
