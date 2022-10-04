import time
import pyautogui as pa
import random
import datetime

currentDT = datetime.datetime.now()
hour = currentDT.hour

people_to_send = ['Ali Dorm Aytac']
mesajlar = ['Sabahin xeyir gozel, netersen?', 'Sabahin xeyir mama necesen', 'Durmusanmi seker qiz?', 'neynirsen mamuska?']
gunluk_mesaj = random.choice(mesajlar)

pa.moveTo(819,1059)
pa.click(button='left')
time.sleep(10)
for people in people_to_send:
    pa.moveTo(230, 110)
    pa.click(button='left')
    pa.write(people)
    pa.press('enter')
    time.sleep(1)
    pa.moveTo(745,997)
    pa.click(button='left')
    pa.write(gunluk_mesaj)
    pa.press('enter')
    time.sleep(2)

time.sleep(10)
pa.moveTo(1891,8)
pa.click(button='left')

time.sleep(60*60)