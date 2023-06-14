from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import xlsxwriter
import time

def get_title():
    column = 1
    row = 1
    titles = driver.find_elements(By. CLASS_NAME, "entry-title")
    for title in titles:
        fin_title = title.text
        print("title", fin_title, column, row)
        row += 1

def get_description():
    column = 1
    row = 1
    descriptions = driver.find_elements(By. CLASS_NAME, "entry-content")
    for description in descriptions:
        fin_description = description.text
        print("Description", fin_description, column, row)
        row += 1

def get_rest():
    header_list = []
    info_list = []
    row = 1
    column = 1
    headers = driver.find_elements(By. CLASS_NAME, "govuk-table__header")
    for header in headers:
        header_list.append(header.text)
    infos = driver.find_elements(By. CLASS_NAME, "govuk-table__cell")
    for info in infos:
        info_list.append(info.text)
    for subheading in range(len(header_list)):
        if header_list[subheading] == "Opportunity status:":
            column = 3
            print(info_list[subheading], row, column)
        if header_list[subheading] == "Funders:":
            column = 4
            print(info_list[subheading], row, column)
        if header_list[subheading] == "Co-funders:":
            column = 4
            print(info_list[subheading], row, column)
        if header_list[subheading] == "Funding type:":
            column = 5
            print(info_list[subheading], row, column)
        if header_list[subheading] == "Total fund:":
            column = 6
            print(info_list[subheading], row, column)
        if header_list[subheading] == "Publication date:":
            column = 7
            print(info_list[subheading], row, column)
        if header_list[subheading] == "Opening date:":
            column = 8
            print(info_list[subheading], row, column)
        if header_list[subheading] == "Closing date:":
            column = 9
            print(info_list[subheading], row, column)
            row += 1

    
def run():
    get_title()
    get_description()
    get_rest()
    
#Scraping functions
#Firebase populating
#run
s = Service(r"C:\Users\Matt\Documents\Scraping\chromedriver.exe")
driver = webdriver.Chrome(service=s)
#1 page export to excel, next
url = "https://www.ukri.org/opportunity/"
#change to iterating pages
driver.get(url)

CLASS_NAME = "class name"

run()
