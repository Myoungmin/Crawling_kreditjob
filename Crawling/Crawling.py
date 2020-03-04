import gspread
from oauth2client.service_account import ServiceAccountCredentials

from selenium import webdriver
from bs4 import BeautifulSoup

scope = ['https://spreadsheets.google.com/feeds', 
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/ko/Desktop/Crawling/my_key.json', scope)

gc = gspread.authorize(creds).open("company test")

worksheet = gc.worksheet('시트1')

worksheet.resize(12, 13)

for i in range(11):

    driver = webdriver.Chrome('/Users/ko/Desktop/Crawling/chromedriver')

    driver.implicitly_wait(3)

    driver.get(worksheet.acell('A' + str(i + 2)).value)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    company_name = soup.find_all(class_='company-name')
    textData = soup.find_all(class_='textData')
    cat_text = soup.find_all(class_='cat_text')
    company_info_data = soup.find_all(class_='company-info-data')
    company_info_ratio = soup.find_all(class_='company-info-ratio')
    sales_data = soup.find_all(class_='sales-data')
    salary_data = soup.find_all(class_='salary-data')

    name = company_name[0].get_text()               #   이름
    top_per = textData[0].get_text()                #   연봉상위
    address = cat_text[0].get_text()                #   소재지
    industry_sector = cat_text[1].get_text()        #   산업군 
    people = company_info_data[0].get_text()        #   인원
    histroy = company_info_data[1].get_text()       #   업력
    join = company_info_ratio[0].get_text()         #   입사율
    resignation = company_info_ratio[1].get_text()  #   퇴사율
    total_sales = sales_data[0].get_text()          #   총매출액
    per_sales = sales_data[1].get_text()            #   1인당 매출액
    percent_of_income = sales_data[2].get_text()    #   매출액 대비 임금비율
    average_income = salary_data[0].get_text()      #   올해 입사자 평균연봉

    worksheet.append_row(['', name, top_per, address, industry_sector, people, histroy, 
                          join, resignation, total_sales, per_sales, percent_of_income,
                          average_income])