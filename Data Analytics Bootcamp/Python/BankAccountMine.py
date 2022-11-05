
class Bank:

    def __init__(self, bank_budcesi):
        self.bank_budcesi = bank_budcesi
        self.proqrami_sonlandir = False

    def salamlama_sehifesi(self):
        print('ElnurBank a xos gelmisiniz!\nZehmet olmasa heyata kecirmek istediyiniz emeliyyati secin:')
        self.secim = input('1. Borc al\n2. Deposit qoy\nSecim: ')

    def borc_hesab_yoxla(self):
        pass

    def deposit_hesab_yoxla(self):
        pass

    def son_yoxla(self):

        sonlandir = input('1. Proqrami sonlandir\n2. Proqrami yeniden baslat\nSecim: ')
        if sonlandir == '1':
            self.proqrami_sonlandir = True
        else:
            self.proqrami_sonlandir = False

    def esas(self):

        while not self.proqrami_sonlandir:
            self.salamlama_sehifesi()

            if self.secim == '1':
                self.borc_hesab_yoxla()
            elif self.secim == '2':
                self.deposit_hesab_yoxla()
            else:
                print('sehv secim etmisiniz zehmet olmasa duzgun secim edin')

            self.son_yoxla()


bank = Bank(10000)
bank.esas()
