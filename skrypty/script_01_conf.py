#plik konfiguracyjny - prosze sprwadzic czy zgadzają się parametry
#domyslnie skonfigurowany do struktury katalogów projektu wiec nie ma koniecznosci nic zmieniac
#dopiero podczas dodawania nowych rocznikow itp
#zeby podaj nazwy interesujacych kolumn i ich nazw jesli sa inne niz te zdefiniowane
#do tej pory, a tam byly w sumie 3 przypadki - przedzialy czasowe - prosze sie upewnic

#lokalizacja katalogu z rocznikami
path_to_folder_ceny_akcji = '../dane_otrzymane/ceny akcji i liczba/'
#lokaliacja katalogu z indywdaualnymi arkuszami z informacjami o pasywach
path_to_folder_spolki_gpw = '../dane_otrzymane/Spółki GPW bez banków i zakładów ubezpieczeń_listopad 2019/'

#parametry dotycza lokalizacji raportow o brakach w danych plikach
folder_braki = 'braki'
brak_daty_bilansowej_file = 'brak_daty_bilansowej.txt'
brak_na_liscie_wartosci_rynkowej_file = 'brak_na_liscie_wartosci_rynkowej.txt'


#podanie sciezki gdzie bedzie zapissywany raport, gdy dana spolka nie posiada inforamcji dla danej daty bilansowej,
#bo te firmy istnieja od roznych momentow
file_with_list_of_company_xlsx = 'brak_daty_bilansowej.txt'

#vector_structure_and_changes
big_vector = 'big_vector'

#vector_structure
small_vector = 'small_vector'

company_pasywa_list_filename = 'pasywa_prev_and_next'
pasywa_prev_filename = 'pasywa_prev'

#dotyczy plików ze strukturą początkową (kapitałową)
my_sheet = 'YS'
#wiersze z których cztamy wartosci, kolumna bedzie potem i bedzie dotyczyla daty bilansowej
poprawka_na_numeracje_wierszy = -2
use_rows = []

for row in [29,60,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,79,80,82,83,84,85,86,87,88,89,90,91,92]:
    use_rows.append(row+poprawka_na_numeracje_wierszy)

#naglowki kolumn - kolejne wiersze brane pod uwage z arkusza YS
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

#folder 2012-2013
#instnieje korelacja miedzy wartosciami rocznik_1, rocznik_2 a kluczami w słowniku roczniki
daty_bilansowe = ['2012-12-31','2013-12-31']
rocznik_1 = '2013'
rocznik_2 = '2014'


roczniki = {
    '2013':'Rocznik_2014__GR.xls',
    '2014':'Rocznik_2015__GR.xls',
    '2015':'Rocznik_2016__GR.xls',
    '2016':'Rocznik_2017_GR.xls',
    '2017':'Rocznik_2018_GR.xls',
    '2018':'Rocznik_2019_GR.xls'
}

brak_daty_bilansowej = []
brak_na_liscie_wartosci_rynkowej = []


wartosc_rynkowa_dict = {}
#przechowuje klucze-nazwy firm i wartosci-liste kluczy {rok1: pasywa_rok1}
company_dict_pasywa_list = {}
vector_change_with_market_value = {}


lista_plikow_do_usuniecia_przed_rozpoczeciem = [
    # 'brak_daty_bilansowej.txt', #ta lista moze posluzyc do przeszukania firm z inną datą bilansową
    'brak_na_liscie_wartosci_rynkowej.txt',
    'pasywa_prev_and_next.json',
    'pasywa_prev_with_market_value.txt',
    'pasywa_prev_with_market_value.xlsx',
    'pasywa_prev.txt',
    'pasywa.txt',
    'vectors.json',
    'vectors.txt',
    'vectors.xlsx'
]

from pathlib import Path
#folder na wyniki
folder_result = 'result'
#sprawdzenie istennienia folderu na wyniku
Path(folder_result).mkdir(parents=True, exist_ok=True)
folder_rocznik = '%s/%d-%d' %(folder_result,int(rocznik_1)-1,int(rocznik_2)-1)
#sprawdzenie istennienia folderu na wyniku
Path(folder_rocznik).mkdir(parents=True, exist_ok=True)