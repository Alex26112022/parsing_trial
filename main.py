from src.parser import Parser


def main():
    URL = 'https://kraevoi--krd.sudrf.ru/modules.php?name=sud_delo&srv_num=1&H_date='
    new_parser = Parser(URL, '11.07.2024')
    new_parser.load_info()
    info = new_parser.get_trial_list()


if __name__ == '__main__':
    main()
