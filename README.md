# optimize_capital_struct

Optimization of the capital and property structure
Projekt był uruhcamiany z użyciem: python v3.7.4

Do utworzenia sieci neuronowej zastosowano biblioteke: keras

W projekcie znajdują się foldery:
*  ```dane_otrzymane```
*  ```siec_neuronowa```
*  ```skrypty ```
	* result
		* pliki
		* big_vector.txt
		* pasywa_prev_and_next.json
		* pasywa_prev.txt
		* small_vector.json
		* small_vector.txt
		* small_vector.xlsx
	* braki
		* brak_daty_bilansowej.txt
		* brak_na_liscie_wartosci_rynkowej.txt
*  ```img```
  
  

> funckja jako output zwraca pliki *.txt, *.xslx/*.csv, *.json
> skrypty: skrypty ponumerowane w kolejnosci uruchamiania

generalnei firmy maja jedną i tą samą date bilansową ale zdażają się przypadki, że jest inaczej np.
> 2015-09-30 SYGNITY
>  2013-06-30 AB 

  
```FOLDER SKRYPTY```
Dane konfiguracyjne umieszczono w pliku:

> python3.7 script_01_conf.py

Kolejność uruchamiania skryptów:

> python3.7 script_02_main.py - przetworzenie danych

> python3.7 script_03_concatenate.py - połączenie wielu plików z wektorami w jeden plik

  
`folder: 2012-2013` - tworzy sie dla nastepujacych parametrow (ustawiane w pliku script_01_conf.py)
>daty_bilansowe = ['2012-12-31','2013-12-31']
rocznik_1 = '2013'
rocznik_2 = '2014'

rocznik_1 i rocznik_2 są kluczem w słowniku 'roczniki' i wskazuje nazwe pliku, z którego należy odczytać wartość rynkową:

> roczniki = {
'2013':'Rocznik_2014__GR.xls',
'2014':'Rocznik_2015__GR.xls',
'2015':'Rocznik_2016__GR.xls',
'2016':'Rocznik_2017_GR.xls',
'2017':'Rocznik_2018_GR.xls',
'2018':'Rocznik_2019_GR.xls'
}

****************
```Końcowe uwagi:```
po przejrzeniu konfiguracji
po uruchomieniu main() na ekranie można zobaczyć output - komunikaty - pojawiajasię gdy dlla danej firmy nir mogą zostać wczytane wszystkei dane np.:
* COMPANY.xlsx    nie ma daty bilansowej z dnia:  2012-12-31!
* COMPANY nie jest notowana na liscie wartosci rynkowej dla 2013-12-31

Tego typu informacje sa przechowywane w  folderze 'braki', gdzie podfoldery mają w nazwie godzine o ktorej zostały uruchomione

