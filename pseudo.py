# -*- coding: utf-8 -*-

"""индексы цен производителей промышленных товаров.xlsm
индексы цен производителей на реализованную сельскохозяйственн продукцию.xls
индексы цен производителей cтроительной продукции.xlsx
индексы цен (тарифов) на грузовые перевозки.xls
цены на первичном и вторичном рынках жилья.xls"""

# import openpyxl
import pandas as pd
from modules import read_data

# must use 'sheet' if more than 1 sheet in Excel workbook

source_definitions = [
    {'varname': 'PPI_PROM_ytd',
     'folder': '11 цены производителей',
     'filename': 'индексы цен производителей промышленных товаров.xlsm',
     'sheet': 'пром.товаров',
     'anchor': 'B5',
     'anchor_value': 96.6},
     
    {'varname': 'PPI_CONSTR_ytd',
     'folder': '11 цены производителей',
     'filename': 'индексы цен производителей промышленных товаров.xlsm',
     'sheet': 'строит.продукция',
     'anchor': 'B5',
     'anchor_value': 99.4},

#### MUST CHANGE
     
    {'varname': 'PPI_AGRO_ytd',
     'folder': '11 цены производителей',
     'filename': 'индексы цен производителей на реализованную сельскохозяйственн продукцию.xls',
     'sheet': 'пром.товаров',
     'anchor': 'B5',
     'anchor_value': 99.4},
     
    {'varname': 'PPI_rog',
     'folder': '11 цены производителей',
     'filename': 'цены на первичном и вторичном рынках жилья.xls',
     'sheet': 'пром.товаров',
     'anchor': 'B5'},

    {'varname': 'PPI_rog',
     'folder': '11 цены производителей',
     'filename': 'цены на первичном и вторичном рынках жилья.xls',
     'sheet': 'пром.товаров',
     'anchor': 'B5'}
     ]
     
#### END - MUST CHANGE

sidebar_doc = """Российская Федерация 1
Центральный федеральный округ
Белгородская область
Брянская область
Владимирская область
Воронежская область
Ивановская область
Калужская область
Костромская область
Курская область
Липецкая область
Московская область  2
Орловская область
Рязанская область
Смоленская область
Тамбовская область
Тверская область
Тульская область
Ярославская область
г.Москва  2
Северо-Западный федеральный округ
Республика Карелия
Республика Коми
Архангельская область
в том числе               Ненецкий авт.округ
Архангельская область без авт. округа 3
Вологодская область
Калининградская область
Ленинградская область
Мурманская область
Новгородская область
Псковская область
г.Санкт-Петербург
Южный                   федеральный округ 4
Республика Адыгея
Республика Калмыкия
Краснодарский край
Астраханская область
Волгоградская область
Ростовская область
Северо-Кавказский федеральный округ
Республика Дагестан
Республика Ингушетия
Кабардино-Балкарская Республика
Карачаево-Черкесская Республика
Республика Северная  Осетия - Алания
Чеченская Республика
Ставропольский край
Приволжский               федеральный округ
Республика Башкортостан
Республика Марий Эл
Республика Мордовия
Республика Татарстан
Удмуртская Республика
Чувашская Республика
Пермский край
Кировская область
Нижегородская область
Оренбургская область
Пензенская область
Самарская область
Саратовская область
Ульяновская область
Уральский             федеральный округ
Курганская область
Свердловская область
Тюменская область
в том числе:                     Ханты-Мансийский       авт. округ - Югра
Ямало-Ненецкий             авт. округ
Тюменская область без авт. округов 3
Челябинская область
Сибирский           федеральный округ
Республика Алтай
Республика Бурятия
Республика Тыва
Республика Хакасия
Алтайский край
Забайкальский край
Красноярский край
Иркутская область
Кемеровская область
Новосибирская область
Омская область
Томская область
Дальневосточный федеральный округ
Республика Саха (Якутия)
Камчатский край
Приморский край
Хабаровский край
Амурская область
Магаданская область
Сахалинская область
Еврейская авт.область
Чукотский авт.округ
Крымский федеральный округ
Республика Крым
г. Севастополь"""

# (1) trauncated 'федеральный округ' and whitespace around it
# (2) trauncated region name with witespaces or many words
testable_sidebar_doc = """Российская Федерация
Центральный
Белгородская область
Брянская область
Владимирская область
Воронежская область
Ивановская область
Калужская область
Костромская область
Курская область
Липецкая область
Московская область
Орловская область
Рязанская область
Смоленская область
Тамбовская область
Тверская область
Тульская область
Ярославская область
г.Москва
Северо-Западный
Республика Карелия
Республика Коми
Архангельская область
Ненецкий
Архангельская область без авт. округа
Вологодская область
Калининградская область
Ленинградская область
Мурманская область
Новгородская область
Псковская область
г.Санкт-Петербург
Южный
Республика Адыгея
Республика Калмыкия
Краснодарский край
Астраханская область
Волгоградская область
Ростовская область
Северо-Кавказский
Республика Дагестан
Республика Ингушетия
Кабардино-Балкарская Республика
Карачаево-Черкесская Республика
Осетия - Алания
Чеченская Республика
Ставропольский край
Приволжский
Республика Башкортостан
Республика Марий Эл
Республика Мордовия
Республика Татарстан
Удмуртская Республика
Чувашская Республика
Пермский край
Кировская область
Нижегородская область
Оренбургская область
Пензенская область
Самарская область
Саратовская область
Ульяновская область
Уральский
Курганская область
Свердловская область
Тюменская область
Ханты-Мансийский
Ямало-Ненецкий
Тюменская область
Челябинская область
Сибирский
Республика Алтай
Республика Бурятия
Республика Тыва
Республика Хакасия
Алтайский край
Забайкальский край
Красноярский край
Иркутская область
Кемеровская область
Новосибирская область
Омская область
Томская область
Дальневосточный
Республика Саха (Якутия)
Камчатский край
Приморский край
Хабаровский край
Амурская область
Магаданская область
Сахалинская область
Еврейская авт.область
Чукотский авт.округ
Крымский
Республика Крым
г. Севастополь"""

years = [2009, 2010, 2011, 2012, 2013, 2014, 2015]

actual_sidebar_list = sidebar_doc.split("\n")
testable_region_names = testable_sidebar_doc.split("\n")

for ar, tr in zip(actual_sidebar_list, testable_region_names):
    # print(ar, "=", tr)
    assert tr in ar

testable_district_names = ['Центральный', 'Северо-Западный', 'Южный', 'Северо-Кавказский',
                           'Приволжский', 'Уральский', 'Сибирский', 'Дальневосточный', 'Крымский']
assert len(testable_district_names) == 9

RF = "Российская Федерация"

# read data
doc_name, doc_comment, doc_years, datafile = read_data('230-232 ' + source_definitions[2]['filename'])

# todo: 
# - summable regions

# - regions by district
districts = []
districts_rows = []
for row, nm in enumerate(datafile['Unnamed']):
    if 'федеральный округ' in nm:
        districts.append(nm)
        districts_rows.append(row)

center_district = datafile.iloc[districts_rows[0]:districts_rows[1]].reset_index(drop=True)
north_west_district = datafile.iloc[districts_rows[1]:districts_rows[2]].reset_index(drop=True)
south_district = datafile.iloc[districts_rows[2]:districts_rows[3]].reset_index(drop=True)
north_caucasus_district = datafile.iloc[districts_rows[3]:districts_rows[4]].reset_index(drop=True)
volga_district = datafile.iloc[districts_rows[4]:districts_rows[5]].reset_index(drop=True)
ural_district = datafile.iloc[districts_rows[5]:districts_rows[6]].reset_index(drop=True)
siberia_district = datafile.iloc[districts_rows[6]:districts_rows[7]].reset_index(drop=True)
far_eastern_district = datafile.iloc[districts_rows[7]:districts_rows[8]].reset_index(drop=True)
crimea_district = datafile.iloc[districts_rows[8]:].reset_index(drop=True)

# Test districts names
assert testable_district_names[0] in center_district['Unnamed'][0]
assert testable_district_names[1] in north_west_district['Unnamed'][0]
assert testable_district_names[2] in south_district['Unnamed'][0]
assert testable_district_names[3] in north_caucasus_district['Unnamed'][0]
assert testable_district_names[4] in volga_district['Unnamed'][0]
assert testable_district_names[5] in ural_district['Unnamed'][0]
assert testable_district_names[6] in siberia_district['Unnamed'][0]
assert testable_district_names[7] in far_eastern_district['Unnamed'][0]
assert testable_district_names[8] in crimea_district['Unnamed'][0]


# Test regions names
for test_dist, dist in zip(testable_district_names, districts):
    assert test_dist in dist

# Test if all regions are in datafile
for test_nm, nm in zip(testable_region_names, datafile['Unnamed'].values):
    assert test_nm in nm

# Test years
for test_ye, ye in zip(years, doc_years):
    assert str(test_ye) in ye


df = '230-232 ' + source_definitions[2]['filename']
dfile = pd.read_excel(df, skiprows=0, skip_footer=0)

# print(dfile.values[1])


def df_read_check():
    # Test if all regions names are in the opened file
    for test_nm, nm in zip(dfile.values[3:], actual_sidebar_list):
        assert nm in test_nm[0]

    # test_years = [ii for ii in dfile.values[1] for jj in ii if jj.isdigit()]
    # for test_y in dfile.values[1]:
    #     # print(test_y)
    #     name = [(str(ii) + ' год') for ii in years]
    #
    #     if str(test_y) not in name and str(test_y) is not 'nan':
    #         print(test_y)
    #     # Test if all regions names are in the opened file
    #     # assert nm in test_nm[0]

df_read_check()
