import time
from suara import suara_scrap
from cnbcindonesia import cnbcindonesia_scrap
from tempo import tempo_scrap
from detik import detik_scrap
from liputan6 import liputan_scrap

while True:
    print("Started")
    suara_scrap()
    cnbcindonesia_scrap()
    tempo_scrap()
    detik_scrap()
    liputan_scrap()
    print("Done")
    time.sleep(21600)