# optimize_capital_struct
Optimization of the capital and property structure



PROJEKT został wykonany pod systemem linux Mint 19
python: 3.7.4
użyte biblioteki: keras

Opis zawartosci folderow w projekcie:
>dane struktury kapitałowej i majątkowej zawarte w folderach: zawierajaą pliki *.xlsx
>dane przetworzeone: wyniki zapisane w osobnych folderach, zawieraja szereg innych plikow, z ktorych mozna informacje
>skrypty: skrypty ponumerowane w kolejnosci uruchamiania

generalnei wszystkie firmy maja jedną i tą samą date bilansową ale zdażają się pojedyncze przypadki, że coś jest inaczej np 2015-09-30	2016-09-30 np SYGNITY, AB '2013-06-30

Mozna przejrzec katalogi

Start 
to przejscie do katalogu skrypty
opcjonalna zmana parametrow w skrypcie 
python3.7 script_01_conf.py
prosze koniecznie sprawdzic jest tam okreslone jakie dane sa teraz przetwarzane, i gdzie, skad sa brane etc,

uruchomienie 
python3.7 script_02_main.py
sprawdzenie i uruchomienie 
python3.7 script_03_concatenate.py

KOLEJNOŚĆ URUCHAMIANIA SKRYPTÓW I KONFIGURACJA

1.PRZYGOTOWANIE
w pliku conf,py można ustawić parametry typu:

        path_to_folder_ceny_akcji = '../dane_otrzymane/ceny akcji i liczba/'
        path_to_folder_spolki_gpw = '../dane_otrzymane/Spółki GPW bez banków i zakładów ubezpieczeń_listopad 2019/'
        my_sheet = 'YS'
        roczniki = {
            '2013':'Rocznik_2014__GR.xls',
        ...
        }
        
        poprawka = -2
        for row in [29,60,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,79,80,82,83,84,85,86,87,88,89,90,91,92]:
            use_rows.append(row+poprawka)

        lista_plikow_do_usuniecia_przed_rozpoczeciem = []

        file_with_list_of_company_xlsx = 'brak_daty_bilansowej.txt'
        
        

INNE PLIKI POMOCNICZE - tylko w uzasadnionych przypadkach nalezy cos zmieniac:
    save_results.py - funkcje uzywane do zapisywania skladowych
    prepare.py
    

2.URUCHAMIANIE
A) najpierw trzeba zebrać dane z plików xlsx

python3.7 script_02_main.py

B) połączenie plików txt z różnych folderów w jeden zbiór danych

C) otwarcie i zapisanei plików utrzonych z połączenia wektorów i zapisanie w formatach *.csv/ *.xslx

d) dobór parametrów dla sieci (zrobione w ramch pracy - mozna pominąć)
    uruchamianie plikow z 4 parametrami okreslajacymi:
    vec29.py warstwa1 warstwa2 epochs batch_size
    vec58.py warstwa1 warstwa2 epochs batch_size
    
    do testowania uruchamialem te pliki za pomoca skryptu napisanego w bash
    
    obserwowalem rezultaty dzialania sieci przy zmianie kazdego z 4 parametrów
    
    wytypowalem taki uklad, ktory daje najblizsze wyniki wzgledem 5 ostatnich vectorow, ktore dla pewnosci usunalem ze zbiorczego zestawienia przed wczytaniem
    
    wygenerowalem wykresy accurance i loss
    
    
e) testowanie zapisanych juz sieci




Dla folderów zastosowano następujące ustawienia:

    folder: 2012-2013
        daty_bilansowe = ['2012-12-31','2013-12-31']
        rocznik_1 = '2013'
        rocznik_2 = '2014'

    folder: 2013-2014
        daty_bilansowe = ['2013-12-31','2014-12-31']
        rocznik_1 = '2014'
        rocznik_2 = '2015'

    folder: 2014-2015
        daty_bilansowe = ['2014-12-31','2015-12-31']
        rocznik_1 = '2015'
        rocznik_2 = '2016'

    folder: 2015-2016
        daty_bilansowe = ['2015-12-31','2016-12-31']
        rocznik_1 = '2016'
        rocznik_2 = '2017'

    folder: 2016-2017
        daty_bilansowe = ['2016-12-31','2017-12-31']
        rocznik_1 = '2017'
        rocznik_2 = '2018'



Rocznik jest kluczem w słowniku 'roczniki' i wskazuje nazwe pliku, z którego odczytano wartość rynkową:
    
    roczniki = {
        '2013':'Rocznik_2014__GR.xls',
        '2014':'Rocznik_2015__GR.xls',
        '2015':'Rocznik_2016__GR.xls',
        '2016':'Rocznik_2017_GR.xls',
        '2017':'Rocznik_2018_GR.xls',
        '2018':'Rocznik_2019_GR.xls'
    }



                                 