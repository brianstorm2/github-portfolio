from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import xlsxwriter
from time import perf_counter

def run_scrape(username):
    
    #collecting tweets
    url = "https://twitter.com/"+username
    try:
        driver.get(url)
    except:
        print('Scraper cannot find this account. Please restart the program')
        exit()
    time.sleep(2)
    collect_data(tweets_list)
    
    #collecting likes
    url = "https://twitter.com/"+username+"/likes"
    driver.get(url)
    time.sleep(2)
    collect_data(likes_list)
    
    #collecting replies
    url = "https://twitter.com/"+username+"/with_replies"
    driver.get(url)
    time.sleep(2)
    collect_data(replies_list)

def collect_data(list_category):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    #grabbing 100 most recent tweets
    while len(list_category) < 100:
        start_time = perf_counter() + 60*5
        tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweetText"]')
        for tweet in tweets:
            #filtering out image tweets, duplicates, extra characters
            if tweet.text not in list_category and tweet.text != '':
                tweet = tweet.text.replace('\n', '')
                list_category.append(tweet)
            else:
                pass
        #if counter exceeds 5 minutes, indication there is no more data to collect, but we allow it to run in case the page needs to be loaded in
        if perf_counter() > start_time:
            print('No more results')
            break

        #amount you need to scroll to access new tweets
        driver.execute_script("window.scrollBy(0, 3350);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        last_height = new_height

def data_output(username):
    #output scrape to excel
    worksheet.write('A1', username)
    worksheet.write('A2', 'Tweets')
    worksheet.write('B2', 'Likes')
    worksheet.write('C2', 'Replies')
    for row_number in range(3, 104):
        tweet_cell = 'A'+str(row_number)
        likes_cell = 'B'+str(row_number)
        replies_cell = 'C'+str(row_number)
        try:
            worksheet.write(tweet_cell, tweets_list[row_number-3])
        except:
            print('There are no more tweets')
        try:
            worksheet.write(likes_cell, likes_list[row_number-3])
        except:
            print('There are no more likes')
        try:
            worksheet.write(replies_cell, replies_list[row_number-3])
        except:
            print('There are no more replies')


options = Options()
options.add_argument("--headless=new")
s = Service(r"C:\Users\Matt\Documents\Scraping\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

CLASS_NAME = "class name"
TAG_NAME = "tag name"
CSS_SELECTOR = "css selector"
XPATH = 'xpath'

tweets_list = []
replies_list = []
likes_list = []

username = input('Enter the username (without \'@\')of the account you want scraped:')
run_scrape(username)

workbook_name = username+"TwitterScrape.xlsx"
workbook = xlsxwriter.Workbook(workbook_name)
worksheet = workbook.add_worksheet()

data_output(username)

workbook.close()
driver.close()
