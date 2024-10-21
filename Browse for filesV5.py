from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
import pandas as pd
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
import openpyxl
import time
import CalcFunctionsV4 #Module made by Matthew Parsons

start_time = time.time()

class StartLabel(Label):
    def __init__(self,master,**config):
        super(StartLabel, self).__init__(master,**config)
        self.config(font='Calibri', fg='#003b70', bg='white')

class StartButton(Button):
    def __init__(self,master,**config):
        super(StartButton, self).__init__(master,**config)
        self.config(font='Calibri', fg='white', bg='#003B70', width=30)
        
class fileParse(object):
    def __init__(self, file_name, text_path):
        self.__file_name = None
        self.__text_path = None
    def get_filename(self):
        open_file = filedialog.askopenfilename()
        file_name = os.path.basename(open_file) #Changing a path to just the filename
        self.__file_name = file_name
    def set_path(self):
        self.__text_path = StartLabel(root, text=self.__file_name)
        self.__text_path.grid(row=2, column=2)
        return self.__text_path
    def clear_func(self):
        self.__file_name = None
        try:
            self.__text_path.destroy()
        except:
            None
    def start_func(self):
        try:
            start_time = time.time()
            calc_workbook = openpyxl.load_workbook(self.__file_name)
            exposure_write = calc_workbook['Exposure'] #For writing data
            calculation_file = pd.ExcelFile(self.__file_name) #For reading data
            messagebox.showinfo('Starting', 'Calculations Starting')
            exposure_sheet = pd.read_excel(calculation_file, 'Exposure') #Selecting different sheets 
            rows_exposure = len(exposure_sheet.index)
            columns_exposure = len(exposure_sheet.columns)
            EE_sheet = pd.read_excel(calculation_file, 'EE')
            lists_sheet = pd.read_excel(calculation_file, 'Lists')
            optima_sheet = pd.read_excel(calculation_file, 'Optima')
            volatility_sheet = pd.read_excel(calculation_file, 'Volatility Haircuts')
            rows_volatility = len(volatility_sheet.index)
            rows_optima = len(optima_sheet.index)
            rows_lists = len(lists_sheet.index)
            pie_sheet = calc_workbook['Pie Chart']
            #**** https://stackoverflow.com/questions/36582460/how-to-clear-a-range-of-values-in-an-excel-workbook-using-openpyxl
            for row in pie_sheet['A4:B7']: #Clear
                for cell in row:
                    cell.value = None
            #****
            root.destroy()
            CalcFunctionsV4.run_program(rows_exposure, exposure_sheet, exposure_write, optima_sheet, EE_sheet, columns_exposure, calc_workbook, pie_sheet, lists_sheet, rows_lists, volatility_sheet, rows_volatility)
            calc_workbook.save(self.__file_name)
            calc_workbook.close()
            new_time = time.time()
            time_taken = (new_time-start_time)
            total_time = round(time_taken, 2)
            messagebox.showinfo('Seconds taken to run', total_time)
        except:
            messagebox.showerror('Error', 'Select a valid file before starting')

root = Tk()
root.title('Capital Requirements Reporting')

file = fileParse('file_name', 'text_path')

browse = StartButton(root, text='Browse', command=lambda:[file.get_filename(), file.set_path()], bg='white')
browseLabel = StartLabel(root, text='Select a file:')
browseLabel.grid(row=2, column=0)
browse.grid(row=2, column=1)

clear = StartButton(root, text='Clear', command=lambda:file.clear_func(),bg='white')
clearLabel = StartLabel(root, text='Press clear to choose a different file:')
clearLabel.grid(row=3, column=0)
clear.grid(row=3, column=1)

start = StartButton(root, text='Start Calculations',command=lambda:file.start_func(), bg='white')
start.grid(row=4, column=1)

root.config(bg='white')    
root.mainloop()

