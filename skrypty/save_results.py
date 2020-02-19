import json
from datetime import datetime
import xlsxwriter
from script_01_conf import *



def save_dict_as_json(data,file_name):
    path_to_file_in_folder_rocznik = "%s/%s"%(folder_rocznik,file_name)
    with open(path_to_file_in_folder_rocznik, 'w') as f:
        json.dump(data, f, ensure_ascii=False,indent=4)


def save_vector_dict_as_txt(data,file_name):
    path_to_file_in_folder_rocznik = "%s/%s"%(folder_rocznik,file_name)
    with open(path_to_file_in_folder_rocznik, 'w') as f:
        for company,roczniki in data.items():
            for value in roczniki:
                f.write('%.4f,'%value)
            f.write('\n')


def save_pasywa_prev_as_txt(data,rok,file_name):
    path_to_file_in_folder_rocznik = "%s/%s"%(folder_rocznik,file_name)
    with open(path_to_file_in_folder_rocznik, 'w') as f:
        for company,roczniki in data.items():
            for value in roczniki[rok]:
                f.write('%.4f,'%value)
            f.write('\n')


def save_pasywa_prev_with_market_value(company_dict_pasywa_list,vector_change_with_market_value,rok,file_name):
    path_to_file_in_folder_rocznik = "%s/%s"%(folder_rocznik,file_name)
    vector = []
    
    for company,rocznik in company_dict_pasywa_list.items():
        temp = rocznik[rok]
        temp += vector_change_with_market_value[company]
        vector.append(temp)
    # print(vector)
    with open(path_to_file_in_folder_rocznik, 'w') as f:
        for item in vector:
            for value in item:
                f.write('%.4f,'%value)
            f.write('\n')


#zapisanie wektora do pliku xlsx z naglowkami (dla small vector)
#to bardziej dla nas
#wlasciwy plik csv z samymi wartosciami - plik wczytywany przez siec - powstawje z dzialania concatenate.py
def save_dict_as_xslx(data,file_name):

    path_to_file_in_folder_rocznik = "%s/%s"%(folder_rocznik,file_name)

    workbook = xlsxwriter.Workbook(path_to_file_in_folder_rocznik)
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': 1})

    for i in range(len(column_header)):

        head_column =''
        if i > 0:
            id_znak = i% len(litery_kolumn)
        if i < len(litery_kolumn):
            head_column = litery_kolumn[i]
        else:
            head_column = 'A' + litery_kolumn[id_znak]

        worksheet.write(head_column,column_header[i],bold)


    # Start from the first cell below the headers.
    row = 1
    col = 0
    
    for company,vector in data.items():
        # wartosci = list(map(float,vector[1:]))
        worksheet.write_string(row, col,     company)
        for i in range(len(vector)):
            worksheet.write_number(row, col + i+1, vector[i])

        row += 1

    workbook.close()
