from bank_logo import logo
import pandas as pd


class Bank:

    def __init__(self, budce_azn, budce_dollar):
        self.budce_azn = budce_azn
        self.budce_dollar = budce_dollar
        self.df = pd.read_csv('depositler.csv')

    def salamlama(self):
        print(logo)
        print('ElnurBanka Xos gelmisiniz!')
        print('Zehmet olasa heyata kecirmek istediyiniz emeliyyati secin:')
        print('1. Borc al')
        print('2. Deposit qoy')
        self.secim = input('Secim: ')

    def borc_al(self):
        print('borc al cagirildi')

    def deposit_qoy(self):
        # print('deposit qoy cagirildi')
        print('6 ay -> 3%\n12 ay -> 6%')
        self.davam_et = input('Davam etmek isteyirsinizmi?(Beli/Xeyr)\n').lower()
        if self.davam_et == 'beli':
            self.ad = input('Adiniz: ')
            self.soyad = input('Soyadiniz: ')
            self.miqdar = int(input('Miqdari yazin: '))
            self.valyuta_novu = input('Valyuta Novu(AZN/USD): ')
            self.muddet = int(input('Muddet ayla(6/12): '))

            self.df.append({'ad':self.ad,'soyad':self.soyad,'miqdar':self.miqdar,'valyuta_novu':self.valyuta_novu,'muddet':self.muddet}, ignore_index=True)
            self.df.to_csv('depositler.csv', index=False)
        elif self.davam_et == 'xeyr':
            pass
        else:
            print('Siz sehv secim etmisiniz.')


    def report(self):
        self.kod = input('Kodu yazin: ')
        if self.kod == '1234':
            print(f'Bankda olan pul miqdari:\nAZN{self.budce_azn}\nUSD{self.budce_dollar}')
            print(self.df)

        else:
            print('Kod yalnisdir')

    def esas(self):

        while True:
            self.salamlama()

            if self.secim == '1':
                self.borc_al()
            elif self.secim == '2':
                self.deposit_qoy()
            elif self.secim == 'report':
                self.report()
            else:
                print('Sehv secim etdiniz. Proqram sonlandirilir')
                break


            self.sonlandir = input('1. Proqrami sonlandir\n2. Proqrami yeniden baslat\nSecim: ')

            if self.sonlandir == '1':
                print('Bankimizdan istifade etdiyiniz ucun cox sagolun')
                break
            elif self.sonlandir == '2':
                print('Bankimizdan istifade etdiyiniz ucun cox sagolun')
                pass
            else:
                print('Sehv secim etmisiniz. Proqram yeniden basladilir')


bank = Bank(100000, 50000)

bank.esas()
