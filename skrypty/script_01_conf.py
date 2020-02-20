'''
*******************************************************************************
                            PLIK KONFIGURACYJNY
*******************************************************************************

DOSTARCZONA Z PROJEKTEM KONFIGURACJA POZWALA NA URUCHOMIENIE SKRYPTOW
*   w razie potrzeby prosze dostosowywać parametry do swoich potrzeb

STRUKTURA PLIKU:

1)  lokalizacja katalogow z dostarczonymi danymi *.xlsx
2)  foldery i pliki do których zapisywany jest output
3)  tworzenie katalogów 
4)  zmienne - bez potrzeby modyfikacji


[UWAGA!]    TO JEST KOMETARZ-INSTRUKCJA 
[UWAGA!]    (PROSZE NIE ODKOMENTOWYWAC ALE ODSZUKAĆ TE ZMIENNE ODPOWIEDNIO DALEJ)
[UWAGA!]    Przykladowe parametry dla danych bilansowych z 2012 i 2013
[UWAGA!]    DANE WOWCZAS ZOSTANA ZAPISANE W KATALOGU 2012-2013
[UWAGA!]        daty_bilansowe = ['2012-12-31','2013-12-31']
[UWAGA!]        rocznik_1 = '2013'
[UWAGA!]        rocznik_2 = '2014'


Kolejno wymienione pliki korzystają z danych umieszczonych w tym pliku:
    
    script_02_main.py
    prepare.py
    save_results.py


*******************************************************************************
'''


'''
ISNIEJE zaleznosc miedzy wartosciami rocznik_1, rocznik_2 a kluczami w slowniku roczniki!

z umieszczonych ponizez: daty_bilansowe i rocznik_1 i rocznik_2
mozna odkomentowywac jeden 'blok' i zakomnetowac inny
i puszczac generacje wektorow, ktore beda zapisywaly sie w katalogu result
do osobnych podfolderow


trzeba uwazac zeby nie nadpisac danych,bo: jesli wywolamy jeszcze raz program, 
zmienimy tylko date bilansową to stracimy te poprzednie wyniki,
chyba ze zmienimy nizej w parametrze nazwe folderu dla wynikow dodajac jakis znak
'''



# daty_bilansowe = ['2012-12-31','2013-12-31']
# rocznik_1 = '2013'
# rocznik_2 = '2014'

# daty_bilansowe = ['2013-12-31','2014-12-31']
# rocznik_1 = '2014'
# rocznik_2 = '2015'

# daty_bilansowe = ['2014-12-31','2015-12-31']
# rocznik_1 = '2015'
# rocznik_2 = '2016'


# daty_bilansowe = ['2015-12-31','2016-12-31']
# rocznik_1 = '2016'
# rocznik_2 = '2017'

daty_bilansowe = ['2016-12-31','2017-12-31']
rocznik_1 = '2017'
rocznik_2 = '2018'


'''
[UWAGA!] W dostarczonym zbiorze nie ma jeszcze danych rocznika dla klucza:
     '2019':'Rocznik_2012_GR.xls'! 
'''
# daty_bilansowe = ['2017-12-31','2018-12-31']
# rocznik_1 = '2018'
# rocznik_2 = '2019'

'''
*******************************************************************************
ad.1)   lokalizacja katalogow z danymi *.xlsx
*******************************************************************************
'''

path_to_folder_ceny_akcji = '../dane_otrzymane/ceny akcji i liczba/'

roczniki = {
    '2013':'Rocznik_2014__GR.xls',
    '2014':'Rocznik_2015__GR.xls',
    '2015':'Rocznik_2016__GR.xls',
    '2016':'Rocznik_2017_GR.xls',
    '2017':'Rocznik_2018_GR.xls',
    '2018':'Rocznik_2019_GR.xls'
}


'''katalog z arkuszami *.xlsx,'''
path_to_folder_spolki_gpw = '../dane_otrzymane/Spółki GPW bez banków i zakładów ubezpieczeń_listopad 2019/'
my_sheet = 'YS'

use_rows = []
poprawka_na_numeracje_wierszy = -2

for row in [29,60,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,79,80,82,83,84,85,86,87,88,89,90,91,92]:
    use_rows.append(row+poprawka_na_numeracje_wierszy)

'''
column_header i litery_kolumn są przydatne do zapisania small_vector
pozwalają wskazać konkretne komórki i nadać im nagłówki
'''
column_header = [
    'Nazwa',
    'Kapitał podstawowy',
    'Należne wpłaty na kapitał podstawowy',
    'Akcje/udziały własne',
    'Kapitał zapasowy',
    'Wyceny i różnice kursowe',
    'Pozostałe kapitały',
    'Zyski zatrzymane / niepokryte straty',
    'Udziały niekontrolujące',
    'Długoterminowe zobowiązania z tytułu instrumen...',
    'Długoterminowe kredyty i pożyczki',
    'Długoterminowe zobowiązania z tytułu obligacji',
    'Długoterminowe zobowiązania z tytułu leasingu',
    'Długoterminowe zobowiązania handlowe',
    'Długoterminowe rezerwy na świadczenia pracownicze',
    'Rezerwa z tytułu odroczonego podatku dochodowego',
    'Długoterminowe rezerwy',
    'Pozostałe zobowiązania długoterminowe',
    'Długoterminowe rozliczenia międzyokresowe (zob...',
    'Zobowiązania z tytułu instrumentów pochodnych',
    'Zobowiązania finansowe (kredyty i pożyczki)',
    'Zobowiązania z tytułu obligacji',
    'Zobowiązania z tytułu leasingu',
    'Zobowiązania handlowe',
    'Świadczenia pracownicze',
    'Zobowiązania z tytułu bieżącego podatku',
    'Rezerwy',
    'Pozostałe zobowiązania',
    'Rozliczenia międzyokresowe (zobowiązania)',
    'Zobowiązania związane z aktywami do zbycia i d...',
    'Wartość rynkowa'
]

litery_kolumn = [
    'A1',
    'B1',
    'C1',
    'D1',
    'E1',
    'F1',
    'G1',
    'H1',
    'I1',
    'J1',
    'K1',
    'L1',
    'M1',
    'N1',
    'O1',
    'P1',
    'Q1',
    'R1',
    'S1',
    'T1',
    'U1',
    'V1',
    'W1',
    'X1',
    'Y1',
    'Z1'
]



'''
*******************************************************************************
ad.2)   foldery i pliki do których zapisywany jest output  
*******************************************************************************
'''
folder_braki = 'braki'
brak_daty_bilansowej_file = 'brak_daty_bilansowej.txt'
brak_na_liscie_wartosci_rynkowej_file = 'brak_na_liscie_wartosci_rynkowej.txt'


'''
z zalozenia w pliku brak_daty_bilansowej sa nazwy plikow, ktore nie mialy konkretnej daty bilansowej 
ale mogą miec inna date bilansową i to nalezy sprawdzic
'''
file_with_list_of_company_xlsx = 'brak_daty_bilansowej.txt'



'''
ZMIENNE SLUZACA ZA NAZWY PLIKOW Z ROZNYMI ROZSZERZENIAMI np. txt, json, xlsx
big_vector - vector_structure_and_changes
small_vector - vector structure
'''

big_vector = 'big_vector'
small_vector = 'small_vector'
company_pasywa_list_filename = 'pasywa_prev_and_next'
pasywa_prev_filename = 'pasywa_prev'



'''
*******************************************************************************
ad.3)  TWORZENIE KATALOGOW DO PRZECHOWYWANIA WYNIKOW
*******************************************************************************
'''

from pathlib import Path

folder_result = 'result'
Path(folder_result).mkdir(parents=True, exist_ok=True)

#nazwa jest tworzona w oparciu o wartosci parametrow ricznik_1 i rocznik_2
folder_rocznik = '%s/%d-%d' %(folder_result,int(rocznik_1)-1,int(rocznik_2)-1)
Path(folder_rocznik).mkdir(parents=True, exist_ok=True)


'''
*******************************************************************************
ad.4)  ZMIENNE BEZ POTRZEBY MODYFIKACJI
*******************************************************************************
'''

brak_daty_bilansowej = []
brak_na_liscie_wartosci_rynkowej = []

wartosc_rynkowa_dict = {}
#przechowuje klucze-nazwy firm i wartosci-liste kluczy {rok1: pasywa_rok1}
company_dict_pasywa_list = {}
vector_change_with_market_value = {}



'''
jesli chcemy uzywac funkcji clear_files() trzeba doprecyzowac sciezke dla plikow
'''

lista_plikow_do_usuniecia_przed_rozpoczeciem = [
    # 'brak_daty_bilansowej.txt', #ta lista moze posluzyc do przeszukania firm z inną datą bilansową

]