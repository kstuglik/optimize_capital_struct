import os
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

from script_01_conf import *


def get_list_of_xlsx_files_from_directory(path_to_folder_spolki_gpw):
    list_of_xlsx_files = os.listdir(path_to_folder_spolki_gpw)
    list_of_xlsx_files = [file for file in list_of_xlsx_files if "#" not in file]
    list_of_company_name = [file.replace('.xlsx','') for file in list_of_xlsx_files]
    list_of_company_name.sort()

    return list_of_company_name


def get_list_of_xlsx_files_from_list(file_with_list_of_company_xlsx):
    list_of_xlsx_files = [line.rstrip('\n') for line in open(file_with_list_of_company_xlsx)]
    list_of_xlsx_files = np.unique(list_of_xlsx_files)
    list_of_company_name = [file.replace('.xlsx','') for file in list_of_xlsx_files]
    list_of_company_name.sort()

    return list_of_company_name


def clear_files():
    for file in lista_plikow_do_usuniecia_przed_rozpoczeciem:
        if os.path.exists(file):
            os.remove(file)
        

def wczytaj_rocznik_i_dodaj_do_slownika(year):
#ustalenie lokalizacji pliku konkretnego rocznika,
    full_path_to_xlsx = path_to_folder_ceny_akcji + roczniki[year]

    #ustalmy tabele i kolumny jakich bedziemy uzywac
    if year in ['2017','2018']:
        tab_name_in_sheet = 'Tab 12'
        if year in ['2017']:
            columns = ['Spółka / Company','Liczba akcji / No. of outstanding shares','Wartość rynkowa (mln zł) / Market value (PLN mil.)']
        if year in ['2018']:#ROCZNIK Z PODSUMOWANIEM 2018 czyli w nazwie pliku jest ...2019.xls
            columns = ['Spółka / Company','Liczba akcji / No. of outstanding shares','Wartość rynkowa (mln zł) / Market value (PLN mil.)']
    else:
        tab_name_in_sheet = 'Tab 17'
        if year in ['2016']:
            columns = ['Spółka / Company','Liczba akcji / No. of shares','Wartość rynkowa (mln zł) / Market value (PLN mil.)']
        else:
            columns = ['Spółka / Company','Liczba akcji / No. of shares','Wartość rynkowa (mln zł) / Market value (PLN million)']


    df = pd.read_excel(full_path_to_xlsx, sheet_name = tab_name_in_sheet)
    # This calls the first row for the header
    new_header = df.iloc[1] 
    # take the rest of your data minus the header row
    df = df[3:] 
    # set the header row as the df header
    df.columns = new_header 
    # print(df.columns)

    #na wypadek komunikatu o bledzie zwiazanym z nie odnalezieniem kolumny przygotowuje message
    exception_msg = 'EXCEPTION dla rocznika z podsumowania yearu'

    try:
        df = df[columns]
    except Exception as e:
        print ('%s %s: %s' %(exception_msg,year,e))


    df.dropna(inplace = True) 
    # converting dataframe int dictionary
    data_dict = df.set_index('Spółka / Company').T.to_dict('list')
        
    return data_dict


def initialize_dict_with_market_value(lista_rocznikow):
    for year in lista_rocznikow:
        wartosc_rynkowa_temp = {}
        wartosc_rynkowa_temp = wczytaj_rocznik_i_dodaj_do_slownika(year)
        wartosc_rynkowa_dict[year] = wartosc_rynkowa_temp


def licz_zmiane(value_prev,value_next):
    temp = 100*((value_next-value_prev)/value_prev)
    if value_prev < 0 and value_next <0:
        temp *= -1
    return round(temp,4)


def przygotuj_vector(prev_year,next_year):
    
    try:
        vector = []
        for i in range(len(prev_year)):
            zmiana = 0
            if prev_year[i] != 0 and next_year[i] != 0:
                zmiana = licz_zmiane(prev_year[i],next_year[i])
            vector.append(zmiana)
        
        return vector
    except Exception as e:
        print ('EXCEPTION[przygotuj_vector]: %s' % e)
        return [0]


def load_csv_from_xlsx(path_to_xlsx_file,okres_rozliczeniowy):
    #my_sheet = 'YS' okreslone w pliku configuracyjnym
    #use rows rowniez zdefiniowane w pliku configuracyjnym
    try:
        pasywa = pd.read_excel(path_to_xlsx_file, sheet_name = my_sheet)
        pasywa = pasywa.iloc[ use_rows , : ]
        #pierwsze pole to nazwa spólki a ostatnie wartość, sprawdz nagłówki w pliku konfiguracujnym 
        new_header = pasywa.iloc[0] 
        pasywa = pasywa[1:].fillna(0) 
        pasywa.columns = new_header

        # w use rows pierwsza wartosc to 29 i jak odszukamy w YS wiersz 29 jest nazwany to data bilansowa (patrz w zakladce YS dla konkretnej spolki)
        #sprawdzamy czy w tym wierszy jest szukana przez nas data bilansowa
        pasywa = pasywa[['Data bilansowa',okres_rozliczeniowy]]
        #jesli udalo sie dopasowac date to mamy kolumne z wybranymi wierszami i pierwszy wiersz na pozycji 0 ma PASYWA
        #jesli nie udalo sie dopasowac to wylapany  zostanie wyjatek
        #takie informacje zostana wyswietlone na ekranie chyba ze zakomentujemy,
        #dodatkowo zapisuje braki w specjalnym plku
        pasywa = pasywa.set_index('Data bilansowa').T.to_dict('list')
        return pasywa

    except Exception as e:
        head, file_name = os.path.split(path_to_xlsx_file)
        brak_daty_bilansowej.append('%s'%file_name)
        print('%s\tnie ma daty bilansowej z dnia:\t%s!'%(file_name,okres_rozliczeniowy))
        return 0


def zapisz_listy_pomocnicze_do_plikow():
    #utworzenie podfolderu w folderze braki datowanego czasem tylko wtedy gdy jest co zapisywac
    if len(brak_daty_bilansowej) > 0 or len(brak_na_liscie_wartosci_rynkowej) > 0:
        outputfilename = str(datetime.now().strftime('%H:%M:%S'))
        path_to_braki = "%s/%s/"%(folder_braki,outputfilename )

        #utworzenie folderu
        Path(path_to_braki).mkdir(parents=True, exist_ok=True)

        if len(brak_daty_bilansowej) > 0 :
            with open(path_to_braki+brak_daty_bilansowej_file, 'a') as f:
                for item in set(brak_daty_bilansowej):
                    f.write('%s\n' % item)

        if len(brak_na_liscie_wartosci_rynkowej) > 0:
            with open(path_to_braki+brak_na_liscie_wartosci_rynkowej_file, 'a') as f:
                for item in set(brak_na_liscie_wartosci_rynkowej):
                    f.write('%s\n' % item)


def give_me_vector(pasywa):
    vector = []
    # print(pasywa)
    pasywa_value = pasywa['PASYWA'][0]
    # print(pasywa_value)
    for key,value in pasywa.items():
        if key != 'PASYWA':
            if value == 0:
                vector.append(0)
            else:
                temp = (value[0]/pasywa_value) * 100 
                temp = round(temp,4)
                vector.append(temp)
    return vector


def dodaj_wartosc_rynkowa(rocznik_1,rocznik_2,company):
    message =''
    try:
        value_1 = wartosc_rynkowa_dict[str(rocznik_1)][company][1]
        # print(value_1)
    except Exception as e:
        message += '%s\t%s\n'%(company,rocznik_1)

    try:    
        value_2 = wartosc_rynkowa_dict[str(rocznik_2)][company][1]
        # print(value_2)
    except Exception as e:
        message += '%s\t%s\n'%(company,rocznik_2)    

    if message == '':
        value = licz_zmiane(value_1,value_2)
        return value
    else:
        brak_na_liscie_wartosci_rynkowej.append(message)
        return 'brak'
