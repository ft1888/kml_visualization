import codecs
import os
import pandas as pd
import xlrd
import csv

xlspath = 'C:/Users/fangtao/Desktop/animal_gui/1.xls'
savepath = 'C:/Users/fangtao/Desktop/animal_gui/1.csv'


def xlsx_to_csv():
    workbook = xlrd.open_workbook(xlspath)
    table = workbook.sheet_by_index(0)
    with open(savepath, 'w', encoding='utf_8_sig', newline='') as f:
        write = csv.writer(f)
        for row_num in range(table.nrows):
            row_value = table.row_values(row_num)
            write.writerow(row_value)


if __name__ == '__main__':
    xlsx_to_csv()

# df.to_csv("a.csv",encoding='utf_8_sig',index=True,sep=',')
