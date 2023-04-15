# import pandas lib as pd
import pandas as pd
from os.path import exists
import openpyxl

def get_azure_data():
    row = [1,2,3,4,5,6,7]
    return row

def len_of_excel():     
        
    if (exists('hello.xlsx')==False):
        wb = openpyxl.Workbook() 
        sheet = wb['Sheet']
        sheet.title = 'Sheet1'
        wb.save(filename='hello.xlsx')
        
    dataframe1 = pd.read_excel('hello.xlsx')
    len_excel=len(dataframe1['time'])
    return len_excel

def write_to_excel(len_excel,new_row):

    workbook = openpyxl.load_workbook(filename='hello.xlsx')
    worksheet = workbook['Sheet1'] 
    
    row=len_excel+2
    for col, entry in enumerate(new_row, start=1):
        worksheet.cell(row=row, column=col, value=entry)

    workbook.save('hello.xlsx')

def getdata(cl_name):
    # read by default 1st sheet of an excel file
    dataframe1 = pd.read_excel('hello.xlsx')
    cl_data = list(dataframe1[cl_name])
    data=cl_data[-1]
    return data


