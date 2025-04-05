import argparse


class SetArguments:
    def set_up(self):
        parser = argparse.ArgumentParser(
            prog='orator',
            description='Klient konsolowy do syntezatora mowy.'
        )
        return parser

    def set_arguments(self, parser):
        parser.add_argument('text', nargs='?',
                            help='Tekst do wypowiedzenia lub zapisania do pliku.')
        parser.add_argument('-o', '--output', metavar='nazwa_pliku',
                            help='Nazwa pliku do zapisu wygenerowanego audio.')
        parser.add_argument('-s', '--source', metavar='plik_tekstowy',
                            help='Nazwa pliku tekstowego do odczytu tekstu.')
        parser.add_argument('-p', '--parameter', nargs=2, metavar=('nazwa_parametru', 'wartość'),
                            help='Ustawia parametr syntezatora mowy.')

        return parser

    def start(self):
        parser = self.set_up()
        self.set_arguments(parser)

        return parser
