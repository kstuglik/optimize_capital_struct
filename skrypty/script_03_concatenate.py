import os
import pandas as pd
import csv
from pathlib import Path

#nazwy plików wyjsciowych, wygenerujemy formaty csv i txt
output_file1 = 'all_big_vectors'
output_file2 = 'all_small_vectors'

#pliki, ktore beda se sobą łączone
input_file1 = 'big_vector.txt'
input_file2 = 'small_vector.txt'

main_folder = 'result/'
sub_folders=['2012-2013/','2013-2014/','2014-2015/','2015-2016/','2016-2017/']


def concatenate(main_folder,sub_folders,input_file,output_file):
    filepath= []
    for item in sub_folders:
        filepath.append(main_folder+item+input_file)
    
    lines_seen = set()
    liczba_powtorzen = 0

    with open(main_folder+output_file, 'w') as outfile:
        for fname in filepath:
            try:
                with open(fname) as infile:
                    for line in infile:
                        if line not in lines_seen:  # not a duplicate
                            outfile.write(line)
                            lines_seen.add(line)
                        else:
                            liczba_powtorzen+=1
            except Exception as e:
                continue#TRYB CICHY BEZ POWIADOMIEN
                # print ('Plik: %s nie został odnaleziony!' %fname)

    outfile.close()
    print('liczba rekordow jest:\t%d\tliczba uniknietych powtorzen:\t%d'%(len(lines_seen),liczba_powtorzen))



if __name__=='__main__':

    for ext in ['.txt','.csv']:
        concatenate(main_folder,sub_folders,input_file1,output_file1+ext)
        concatenate(main_folder,sub_folders,input_file2,output_file2+ext)
