from script_01_conf import *

from prepare import *
from save_results import *

'''
    data bilansowa, roczniki i inne ważne parametry są definiowane w pliku konfiguracyjnym! 
'''


def main():

    '''usuniecie plikow - artefaktow - opcjonalne'''

    clear_files()

    '''
    do funkcji initialize_dict_with_market_value() podajemy liste 2 elementową
    '''

    initialize_dict_with_market_value([rocznik_1,rocznik_2])

    '''
    Są trzy sposoby na przetworzenie danych:
    1. wczytanie nazw firm z pliku w którym są wymienione jedna pod drugą, każda w nowym wierszu
        jesli chcemy inaczej to trzeba przejsc do tej funkcji i ustawic inny delimeter, np. zmienic z '\n' na ','
    2. wczytanie nazw z konkretnej lokalizacji (uwaga zeby znajdowały sie tam same pliku *.xlsx)
    3. wczytanie nazwy firmy z listy podanej wprost'''

    #list_of_company_name = get_list_of_xlsx_files_from_list(file_with_list_of_company_xlsx)
    list_of_company_name = get_list_of_xlsx_files_from_directory(path_to_folder_spolki_gpw)
    # list_of_company_name = ['ZYWIEC','AB']

    '''wyswietlenie listy firm, które będą sprawdzane'''
    # print(list_of_company_name)



    '''
    szybki test bez koniecznosci wczytywania wszystkiego z listy:
    zamiast: for company_name in list_of_company_name:
    mozna sprawdzic: for company_name in list_of_company_name[:10]:
    '''



    for company_name in list_of_company_name:
        path_to_xlsx_file = path_to_folder_spolki_gpw + company_name + '.xlsx'


        pasywa_prev = load_csv_from_xlsx(path_to_xlsx_file,daty_bilansowe[0])
        pasywa_next = load_csv_from_xlsx(path_to_xlsx_file,daty_bilansowe[1])


        if pasywa_prev != 0 and pasywa_next != 0:
            temp = dodaj_wartosc_rynkowa(rocznik_1,rocznik_2,company_name)
            if temp != 'brak':

                pasywa_prev = give_me_vector(pasywa_prev)
                pasywa_next = give_me_vector(pasywa_next)

                wektor_3 = przygotuj_vector(pasywa_prev,pasywa_next)
                wektor_3.append(temp)

                company_dict_pasywa_list[company_name] = {(int(rocznik_1)-1):pasywa_prev,rocznik_1:pasywa_next}
                
                #wektor przechowuje informacje o pasywach w roku poprzednik i kolejnym
                vector_change_with_market_value[company_name] = wektor_3
                
                # print(pasywa_prev)
                # print(pasywa_next)
                # print(wektor_3)

            else:
                print('%s nie jest notowana na liscie wartosci rynkowej dla %s'%(company_name,daty_bilansowe[1]))
    
    print('liczba dopasowan:\t%d'%len(company_dict_pasywa_list))


    '''
    Mozemy zdecydowac jakiego typu dane chcemy zapisac do pliku:
    1) slownik wektorow w postaci json
    2) wektor struktury poczatkowej jako plik txt
    3) wektor zmian jako plik txt
    4) struktura poczatkowa i zmiany jako jeden wektor
    5) zapisac informacje o odnotowanych brakach - firmy dla ktorych nie udalo sie uzyskac wektorow
    '''

    '''nazwa pliku small_vector została zdefiniowana w pliku konfiguracyjnym'''
    save_dict_as_xslx(          vector_change_with_market_value,                small_vector+'.xlsx')
    save_vector_dict_as_txt(    vector_change_with_market_value,                small_vector+'.txt')
    save_dict_as_json(          vector_change_with_market_value,                small_vector+'.json')
    #generowanie vectora 59elementowego
    save_pasywa_prev_with_market_value(company_dict_pasywa_list, vector_change_with_market_value,int(rocznik_1)-1,big_vector+".txt")

    #zapisanie do pliku wlasci wartosci składowych z sekcji pasywa dla roku prev i next (nie procentowych zmian)
    save_dict_as_json(          company_dict_pasywa_list,                       company_pasywa_list_filename+'.json')
    save_pasywa_prev_as_txt(    company_dict_pasywa_list,int(rocznik_1)-1,      pasywa_prev_filename+'.txt')



    zapisz_listy_pomocnicze_do_plikow()


if __name__ == '__main__':
    main()