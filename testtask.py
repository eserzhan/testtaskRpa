import pandas as pd
import os
from os import walk

df = pd.DataFrame(columns=('Папка в которой лежит файл', 'Название файла', 'Расширение файла'))


def nameParse(s):
    res = s.split(".")
    if res[0] == "":
        return s
    return res[0]

def extParse(s):
    res = s.split(".")
    if res[0] == "" or len(res) == 1:
        return "emptyExtension"
    return res[-1]

for (dirpath, dirnames, filenames) in walk(os.path.dirname(os.path.realpath(__file__))):
    #print(dirpath.split('\\')[-1], dirnames, filenames)
    for i in dirnames:
        df.loc[len(df.index)] = [dirpath.split('\\')[-1], i, "folder"]
    for i in filenames:
        df.loc[len(df.index)] = [dirpath.split('\\')[-1], nameParse(i), extParse(i)]


df.to_excel(r'result.xlsx')