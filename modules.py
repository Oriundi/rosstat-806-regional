# -*- coding: utf-8 -*-

import pandas as pd


def read_data(data):
    doc_nm = pd.read_excel(data, skiprows=0, skip_footer=1000)
    doc_com = pd.read_excel(data, skiprows=1, skip_footer=1000)
    doc_y = pd.read_excel(data, skiprows=2, skip_footer=1000)

    # test if file reads to DataFrame
    assert isinstance(doc_nm, pd.DataFrame)
    assert isinstance(doc_com, pd.DataFrame)
    assert isinstance(doc_y, pd.DataFrame)

    doc_name = "".join([i for i in doc_nm.keys()[0] if not i.isdigit()])
    doc_comment = doc_com.keys()[0]
    doc_years = [ii for ii in doc_y.keys() if 'год' in ii]

    datafile = pd.read_excel(data, skiprows=3, skip_footer=7)

    # Remove digits from the months names
    new_names = []
    for ii in datafile.keys():
        name = ''
        for jj in ii:
            if jj.isalpha():
                name = name + jj
        new_names.append(name)
    datafile.rename(columns=dict(zip(datafile.keys(), new_names)), inplace=True)

    # Replace space on the end of the region name if exists
    for nm in datafile['Unnamed']:
        new = "".join([i for i in nm if not i.isdigit()])
        datafile.replace(nm, new, inplace=True)
        if nm[-1] == ' ':
            nnm = nm[:-1]
            datafile.replace(nm, nnm, inplace=True)

    return doc_name, doc_comment, doc_years, datafile
